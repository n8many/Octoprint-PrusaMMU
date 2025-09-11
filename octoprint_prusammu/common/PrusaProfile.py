# coding=utf-8
from __future__ import absolute_import

# The command sent on connection to tell us what type of printer we have
class MachineType():
  MK3="MK3S"
  MK3_5="MK3.5"
  MK3_9="MK3.9"
  MK4="MK4"
  COREONE="COREONE"
  XL="Prusa-XL"

  # Print Profile (or the profile of the printer in the gcode)
class PrusaProfile():
  MK3="MK3"
  MK3_5="MK3_5"
  MK3_9="MK3_9"
  MK4="MK4"
  COREONE="COREONE"
  XL="Prusa-XL"

def is_buddy(machine_type):
  if(machine_type==MachineType.MK3):
    return False
  else:
    # all others use buddy firmware
    return True

def has_shared_tool(machine_type):
  if(machine_type==MachineType.XL):
    # has multitool, which changes behavior
    return False
  else:
    # all others have true MMU (until COREONE INDX)
    return True

# Given a machine type it returns the profile type
def detect_connection_profile(machine_type):
  if MachineType.MK3_5 in machine_type:
    return PrusaProfile.MK3_5
  if MachineType.MK3_9 in machine_type:
    return PrusaProfile.MK3_9
  if MachineType.MK4 in machine_type:
    return PrusaProfile.MK4
  if MachineType.COREONE in machine_type:
    return PrusaProfile.COREONE
  if MachineType.XL in machine_type:
    return PrusaProfile.XL
  # Fallback to the MK3
  return PrusaProfile.MK3