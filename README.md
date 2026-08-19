# pyorcasdk

## Introduction

pyorcasdk is a Python package designed to allow for easy software interaction with ORCA Series linear motors. The package is created using Python bindings on our C++ library, [orcaSDK](https://github.com/IrisDynamics/orcaSDK).

## Prerequisites

- Python version 3.8 to 3.14t
- pip
- A Windows or Linux device

## Installation

To install the package, execute this command into your command-line interface:

```
pip install pyorcasdk
```

It is also highly recommended to read the [Setting Up Hardware and Testing Your Motor](https://github.com/IrisDynamics/orcaSDK/#setting-up-hardware-and-testing-your-motor) section of orcaSDK's README to handle hardware setup and platform configuration.

> pyorcasdk depends on C++ runtime shared libraries. On Windows it is possible to install pyorcasdk without these shared libraries. If you encounter the error `ImportError: DLL load failed while importing... ` on Windows, then please install the latest [Microsoft Visual C++ Redistributables](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

## Documentation

Reference documentation for this package can be found [here](https://docs.irisdynamics.com/sdk/pyorcasdk/).

### Examples

Our [tutorial suite](https://docs.irisdynamics.com/sdk/tutorials/) contains examples for a set of common use cases for our motors with this library.

### ORCA Documentation

Our [downloads page](https://irisdynamics.com/downloads) contains multiple files which are useful references for handling the hardware setup for your ORCA motor. The [ORCA Series Reference Manual](https://irisdynamics.com/hubfs/Website/Downloads/Orca/Approved/RM220115_Orca_Series_Reference_Manual.pdf) goes into great detail on all features available in the motor and how the features can be accessed.