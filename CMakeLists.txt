# --------------------------------------------------------------------------
# Dependencies
# --------------------------------------------------------------------------

find_package(yat CONFIG REQUIRED)

# --------------------------------------------------------------------------
# Collect sources adnd includes
# --------------------------------------------------------------------------

file(GLOB_RECURSE sources src/*.cpp)
list(FILTER sources EXCLUDE REGEX ".*/src/imXpadConfig.cpp$")
set(includedirs
	include/
)

# --------------------------------------------------------------------------
# Target
# --------------------------------------------------------------------------

add_library(limaimxpad ${sources})
target_include_directories(limaimxpad 
	PUBLIC 
		${includedirs}
)
target_link_libraries(limaimxpad 
	PUBLIC	
		limacore
        yat::yat
)

limatools_set_library_soversion(limaimxpad "VERSION")

# --------------------------------------------------------------------------
# Compile definitions
# --------------------------------------------------------------------------

file(READ "${CMAKE_CURRENT_SOURCE_DIR}/VERSION" IMXPAD_VERSION_RAW)
string(STRIP "${IMXPAD_VERSION_RAW}" IMXPAD_VERSION)

target_compile_definitions(limaimxpad
    PUBLIC
        IMXPAD_NAME=ImXpad
        IMXPAD_VERSION=${IMXPAD_VERSION}
        IMXPAD_ENABLED
)

message(STATUS "Camera enabled: ImXpad ${IMXPAD_VERSION}")

# --------------------------------------------------------------------------
# Install
# --------------------------------------------------------------------------

install(
    TARGETS limaimxpad 
    LIBRARY DESTINATION lib
)
