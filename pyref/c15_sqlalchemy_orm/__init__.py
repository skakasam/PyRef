from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import ClassVar, Final, final

from sqlalchemy import (
    CheckConstraint,
    Engine,
    Enum,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
    create_engine,
    event,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

POSITIONS: Final = ("HR", "Manager", "Architect", "Developer", "Tester", "Support", "Intern")
DB_PATH = Path(r"D:\Projects\Database\Sqlite\pyref.db")
ENGINE: Engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)
SESSION = sessionmaker(ENGINE)


@event.listens_for(ENGINE, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    """Enables foreign key enforcement for every SQLite connection."""
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Base(DeclarativeBase):
    pass


@final
class Projects(Base):
    # Table
    __tablename__ = "projects"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str | None] = mapped_column(String(200))

    # Constraints
    __table_args__ = {"sqlite_autoincrement": True}

    # Relationships
    allocations: Mapped[list["Allocations"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


@final
class Employees(Base):
    # Table
    __tablename__ = "employees"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    dob: Mapped[date] = mapped_column()
    position: Mapped[str] = mapped_column(Enum(*POSITIONS))
    salary: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    email: Mapped[str] = mapped_column(String(100), unique=True)

    # Constraints
    __table_args__ = (
        CheckConstraint("salary > 0", name="chk_salary_positive"),
        CheckConstraint("email LIKE '%_@__%.__%'", name="chk_email_format"),
        CheckConstraint("dob GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'", name="chk_dob_format"),
        CheckConstraint(f"position IN ({', '.join(repr(pos) for pos in POSITIONS)})", name="chk_position_valid"),
        {"sqlite_autoincrement": True},
    )

    # Relationships
    allocations: Mapped[list["Allocations"]] = relationship(
        back_populates="employee",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


@final
class Allocations(Base):
    # Table
    __tablename__ = "allocations"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"))

    # Constraints
    __table_args__ = (
        UniqueConstraint("employee_id", "project_id", name="uq_employee_project"),
        {"sqlite_autoincrement": True},
    )

    # Relationships
    employee: Mapped["Employees"] = relationship(back_populates="allocations")
    project: Mapped["Projects"] = relationship(back_populates="allocations")


METADATA = Base.metadata

__all__ = ["ENGINE", "SESSION", "METADATA", "Projects", "Employees", "Allocations"]
