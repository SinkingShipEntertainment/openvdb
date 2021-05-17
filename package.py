name = "openvdb"

version = "6.1.0"

description = \
    """
    OpenVDB is an open source C++ library comprising a novel hierarchical data
    structure and a large suite of tools for the efficient storage and manipulation
    of sparse volumetric data discretized on three-dimensional grids.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "tbb-2017.6",
    "blosc-1.5.0",
    "openexr-2.2.0",
]

private_build_requires = [
    "cmake",
    "gcc",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.70.0"]
]

uuid = "repository.openvdb"

def commands():
    env.OPENVDB_LOCATION = "{root}"
    env.OPENVDB_ROOT = "{root}"
    env.OPENVDB_INCLUDE_DIR = "{root}/include"
    env.OPENVDB_LIBRARY_DIR = "{root}/lib"
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PATH.append("{root}/bin")

    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

