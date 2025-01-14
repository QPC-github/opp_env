def get_all_omnetpp_6_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "which", "bison", "flex", "perl", "which", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz",
                "setenv_command": "source setenv",
                "configure_command": "./configure WITH_OSG=no",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["6.0.1", "6.0"]
        ]
    ]

def get_all_omnetpp_5_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz",
                "setenv_command": "source setenv",
                "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["5.7"]
        ],
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src-linux.tgz",
                "setenv_command": "source setenv -f",
                "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["5.6.2", "5.6.1", "5.6", "5.5.1", "5.4.1", "5.3", "5.2.1", "5.2", "5.1.1", "5.1", "5.0"]
        ]
    ]

def get_all_omnetpp_4_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "libxml2", "expat", "xdg-utils" ],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src.tgz",
                "setenv_command": "export PATH=$(pwd)/bin:$PATH && export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && export TCL_LIBRARY=$(echo 'puts [info library]; exit' | wish) && export HOSTNAME && export HOST",
                "configure_command": "unset AR && ./configure",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["4.6", "4.5", "4.4.1", "4.4", "4.3.1", "4.3", "4.2.2", "4.2.1", "4.2", "4.1", "4.0"]
        ]
    ]

def get_all_omnetpp_3_x_versions():
    return [
        {
            "name": "omnetpp", "version": "3.3p1",
            "stdenv": "gcc7Stdenv",
            "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "expat" ],
            "download_url": "https://github.com/omnetpp/omnetpp/releases/download/omnetpp-3.3-ubuntu18.04/omnetpp-3.3-src-gcc73.tgz",
            "patch_command": "sed -i '1s|.*|#!/bin/env perl|;2s|.*||' src/nedc/opp_msgc",
            "setenv_command": "export PATH=$(pwd)/bin:$PATH && export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && export TCL_LIBRARY=$(echo 'puts [info library]; exit' | wish)",
            "configure_command": "./configure",
            "build_command": "make MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_git_versions():
    return [
        {
            "name": "omnetpp", "version": "git",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"],
            "git_url": "git@github.com:omnetpp/omnetpp.git",
            "setenv_command": "source setenv",
            "configure_command": "./configure WITH_OSG=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_versions():
    return [
        *get_all_omnetpp_git_versions(),
        *get_all_omnetpp_6_x_versions(),
        *get_all_omnetpp_5_x_versions(),
        *get_all_omnetpp_4_x_versions(),
        *get_all_omnetpp_3_x_versions(),
    ]
