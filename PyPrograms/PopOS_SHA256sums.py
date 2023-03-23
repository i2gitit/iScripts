import sys
# Author: i
# This program will compare sha256sum of PopOS 22.04 LTS, 
# all three versions has been assigned to CONSTANTS

# CONSTANTS
# sha256sum from Pop OS Website 07/25/2022
POP_OS_2204LTS='b60b55dcf5f7178a78f9c39e199892a01264c953772f5c076a3fb7a5659357c7'
POP_OS_FOR_NVIDIA_2204LTS='897725ca4ee726f1a6ff57a8c0235ab82ba565ba18676b95b326280a8c261546'
POP_OS_FOR_PI_2204LTS='d5a3df97872cc2fbcb6e2a60b1f9205f496135eba223ad423d5327892fae7cb7'


def main():
    # Variables
    msg=''
    #user_sha=''
    user_amd_intel_sha='b60b55dcf5f7178a78f9c39e199892a01264c953772f5c076a3fb7a5659357c7'
    user_amd_NVIDIA_sha='897725ca4ee726f1a6ff57a8c0235ab82ba565ba18676b95b326280a8c261546'
    user_arm_pi_sha='d5a3df97872cc2fbcb6e2a60b1f9205f496135eba223ad423d5327892fae7cb7'

    # INPUT
    # get sha256sum from user
    #user_sha=input('Please input the sha256sum that was generated by your computer:\n')

    # PROCESSING
    if user_amd_intel_sha==POP_OS_2204LTS:
        print('This sha256sum is for Pop OS 22.04 LTS')
    if user_amd_NVIDIA_sha==POP_OS_FOR_NVIDIA_2204LTS:
        print('This sha256sum is for Pop OS 22.04 LTS For NVIDIA equipped Laptops')
    if user_arm_pi_sha==POP_OS_FOR_PI_2204LTS:
        print('This sha256sum is for Pop OS 22.04 LTS for Raspberry Pi')
    else:
        print('This sha256sum did NOT match any sha256sum in this program.')

    # OUTPUT
    print(msg)

if __name__=='__main__':
    sys.exit(main())