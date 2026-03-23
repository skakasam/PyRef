"""Python Named Tuples Practice Module"""

from collections import namedtuple

laptop = "Dell Precision 5550 Laptop"
monitor = "Dell Ultrasharp U2722D QHD Monitor"

###############################################################################
# Named Tuples Creation (from Collections module)
###############################################################################
# Declaration needs a type name (DeskSetup) and field names (in the form of
# a list, or a space or comma separated strings)
###############################################################################
DeskSetup = namedtuple(
    "DeskSetup",
    [
        "laptop",
        "monitor_1",
        "monitor_2",
        "monitor_3",
        "monitor_arm",
        "monitor_riser",
        "dock",
        "webcam",
        "usb_hub",
        "headset",
        "keyboard",
        "mouse",
        "desk",
        "chair",
    ],
)
# Instantiation possible with positional and keyword arguments

desk_setup = DeskSetup(
    laptop,
    monitor,
    monitor,
    monitor_3=None,
    monitor_arm=None,
    monitor_riser="Vaydeer Dual Aluminum Monitor Stand Riser",
    dock="Dell Thunderbolt WD19TBS Dock",
    webcam="Nolansend 4K Webcam",
    usb_hub="Insignia 7-Port USB 2.0 Hub",
    headset="Lenovo Wireless VoIP Headset",
    keyboard="Keychron B6 Pro Wireless Keyboard",
    mouse="Keychron M6 Wireless Optical Mouse",
    desk="SHW 55-Inch Commercial-Grade Office Computer Desk",
    chair="Cykov Ergonomic Mesh Desk Chair",
)

################################################################################
# Accessing Named Tuple Elements
###############################################################################
print("Named Tuple Examples:")
print(f"  type(DeskSetup): {type(DeskSetup)}")
print(f"  type(desk_setup): {type(desk_setup)}")
print(f"  desk_setup: {desk_setup}")
print(f"  Access using field name --> desk_setup.laptop: {desk_setup.laptop}")
print(f"  Access using index      --> desk_setup[0]    : {desk_setup[0]}")

###############################################################################
# Modifying Named Tuples
# Note: Named tuples are immutable, so we can't change their values directly.
# Instead, we create a new instance using _make or _replace methods with the
# desired changes. However, they do not modify the original instance.
###############################################################################
print("Modifying Named Tuples Examples:")
another_desk_setup = DeskSetup._make(desk_setup)
print(f"  another_desk_setup is desk_setup? {another_desk_setup == desk_setup}")
yet_another_desk_setup = desk_setup._replace(monitor_3=monitor)
print(f"  desk_setup is yet_another_desk_setup? {desk_setup == yet_another_desk_setup}")

###############################################################################
# Named Tuple Attributes
###############################################################################
print("Named Tuple Attributes Examples:")
print(f"  desk_setup._fields: {desk_setup._fields}")
print(f"  desk_setup._asdict(): {desk_setup._asdict()}")
print(f"  desk_setup._field_defaults: {desk_setup._field_defaults}")


###############################################################################
# Extending Named Tuples by Inheritance
###############################################################################
# class ExtendedDeskSetup(DeskSetup):
class ExtendedDeskSetup(
    namedtuple(
        "DeskSetup",
        [
            "laptop",
            "monitor_1",
            "monitor_2",
            "monitor_3",
            "monitor_arm",
            "monitor_riser",
            "dock",
            "webcam",
            "usb_hub",
            "headset",
            "keyboard",
            "mouse",
            "desk",
            "chair",
        ],
    )
):
    @property
    def monitors(self):
        """Returns a tuple of all monitors in the desk setup."""
        monitors = []
        if self.monitor_1:
            monitors.append(self.monitor_1)
        if self.monitor_2:
            monitors.append(self.monitor_2)
        if self.monitor_3:
            monitors.append(self.monitor_3)
        return tuple(monitors)

    @property
    def total_monitors(self):
        """Returns the total number of monitors in the desk setup."""
        return len(self.monitors)

    @property
    def monitor_mount(self):
        """Returns the monitor mount used in the desk setup."""
        if self.monitor_arm:
            return "ARM"
        elif self.monitor_riser:
            return "RISER"
        return None


extended_desk_setup = ExtendedDeskSetup(
    laptop=laptop,
    monitor_1=monitor,
    monitor_2=monitor,
    monitor_3=None,
    monitor_arm=None,
    monitor_riser="Vaydeer Dual Aluminum Monitor Stand Riser",
    dock="Dell Thunderbolt WD19TBS Dock",
    webcam="Nolansend 4K Webcam",
    usb_hub="Insignia 7-Port USB 2.0 Hub",
    headset="Lenovo Wireless VoIP Headset",
    keyboard="Keychron B6 Pro Wireless Keyboard",
    mouse="Keychron M6 Wireless Optical Mouse",
    desk="SHW 55-Inch Commercial-Grade Office Computer Desk",
    chair="Cykov Ergonomic Mesh Desk Chair",
)

print("Extending Named Tuples Examples:")
print(f"  extended_desk_setup: {extended_desk_setup}")

###############################################################################
# Extending Named Tuples by another Named Tuple
###############################################################################
NewDeskSetup = namedtuple("NewDeskSetup", extended_desk_setup._fields + ("cooling_pad",))
new_desk_setup = NewDeskSetup(*extended_desk_setup, cooling_pad="Cooler Master NotePal X3")
print("Extending Named Tuples by another Named Tuple Examples:")
print(f"  new_desk_setup: {new_desk_setup}")
