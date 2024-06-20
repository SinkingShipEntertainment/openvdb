name = "openvdb"

version = "9.1.0.sse.2.0.0"

description = \
    """
    OpenVDB is an open source C++ library comprising a novel hierarchical data
    structure and a large suite of tools for the efficient storage and manipulation
    of sparse volumetric data discretized on three-dimensional grids.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "blosc-1.17.0",
    "tbb-2020.3",
    "boost-1.82",
    "openexr-3.1.12",
    "numpy",
]

private_build_requires = [
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
]

uuid = "repository.openvdb"

# run rez-build -i or rez-release with CMake directives:
# rez-build -i -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.OPENVDB_LOCATION = "{root}"
    env.OPENVDB_ROOT = "{root}"
    env.OPENVDB_INCLUDE_DIR = "{root}/include"
    env.OPENVDB_LIBRARY_DIR = "{root}/lib64"
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
