name = "openvdb"

version = "9.1.0.sse.1.0.0"

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
    "blosc-1.17.0",
    "openexr-3.1.5",
    "numpy",
]

private_build_requires = [
]

# TODO: We are specifying the Python versions here just to drive the corrent version
# of boost. But in the CMakeLists.txt, we are not building the Python modules for
# VDB due to an error that I still need to investigate.
variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "tbb-2019.6", "boost-1.76.0"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "tbb-2019.6", "boost-1.76.0"],
]

uuid = "repository.openvdb"

# run rez-build -i or rez-release with CMake directives:
# rez-build -i -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.OPENVDB_LOCATION = "{root}"
    env.OPENVDB_ROOT = "{root}"
    env.OPENVDB_INCLUDE_DIR = "{root}/include"
    env.OPENVDB_LIBRARY_DIR = "{root}/lib64"
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
