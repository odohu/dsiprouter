#!/usr/bin/env bash
#set -x

# NOTES:
# contains utility functions and shared variables
# should be sourced by an external script

###################
# Color constants #
###################

# Ansi Colors
ESC_SEQ="\033["
ANSI_NONE="${ESC_SEQ}39;49;00m" # Reset colors
ANSI_RED="${ESC_SEQ}1;31m"
ANSI_GREEN="${ESC_SEQ}1;32m"
ANSI_YELLOW="${ESC_SEQ}1;33m"
ANSI_CYAN="${ESC_SEQ}1;36m"

##############################################
# Printing functions and String Manipulation #
##############################################

printerr() {
    printf "%b%s%b\n" "${ANSI_RED}" "$*" "${ANSI_NONE}"
}

printwarn() {
    printf "%b%s%b\n" "${ANSI_YELLOW}" "$*" "${ANSI_NONE}"
}

printdbg() {
    printf "%b%s%b\n" "${ANSI_GREEN}" "$*" "${ANSI_NONE}"
}

pprint() {
    printf "%b%s%b\n" "${ANSI_CYAN}" "$*" "${ANSI_NONE}"
}

######################################
# Traceback / Debug helper functions #
######################################

backtrace() {
    local DEPTN=${#FUNCNAME[@]}

    for ((i=1; i < ${DEPTN}; i++)); do
        local FUNC="${FUNCNAME[$i]}"
        local LINE="${BASH_LINENO[$((i-1))]}"
        local SRC="${BASH_SOURCE[$((i-1))]}"
        printf '%*s' $i '' # indent
        printerr "[ERROR]: ${FUNC}(), ${SRC}, line: ${LINE}"
    done
}

setErrorTracing() {
    set -o errtrace
    trap 'backtrace' ERR
}

#######################################
# Reusable / Shared Utility functions #
#######################################

# $1 == attribute name
# $2 == attribute value
# $3 == python config file
# $4 == whether to 'quote' value (use for strings)
setConfigAttrib() {
    local NAME="$1"
    local VALUE="$2"
    local CONFIG_FILE="$3"

    if (( $# >= 4 )); then
        VALUE="'${VALUE}'"
    fi
    sed -i -r -e "s|($NAME[[:space:]]?=[[:space:]]?.*)|$NAME = $VALUE|g" ${CONFIG_FILE}
}

# $1 == attribute name
# $2 == python config file
# returns: attribute value
getConfigAttrib() {
    local NAME="$1"
    local CONFIG_FILE="$2"

    local VALUE=$(grep -oP '^(?!#)(?:'${NAME}')[ \t]*=[ \t]*\K(?:\w+\(.*\)[ \t\v]*$|[\w\d\.]+[ \t]*$|\{.*\}|\[.*\][ \t]*$|\(.*\)[ \t]*$|""".*"""[ \t]*$|'"'''.*'''"'[ \v]*$|".*"[ \t]*$|'"'.*'"')' ${CONFIG_FILE})
    printf "$VALUE" | sed -r -e "s/^'+(.+?)'+$/\1/g" -e 's/^"+(.+?)"+$/\1/g'
}

# $1 == attribute name
# $2 == kamailio config file
enableKamailioConfigAttrib() {
    local NAME="$1"
    local CONFIG_FILE="$2"

    sed -i -r -e "s/#+(!(define|trydef|redefine)[[:space:]]? $NAME)/#\1/g" ${CONFIG_FILE}
}

# $1 == attribute name
# $2 == kamailio config file
disableKamailioConfigAttrib() {
    local NAME="$1"
    local CONFIG_FILE="$2"

    sed -i -r -e "s/#+(!(define|trydef|redefine)[[:space:]]? $NAME)/##\1/g" ${CONFIG_FILE}
}

# $1 == name of ip to change
# $2 == value to change ip to
# $3 == kamailio config file
setKamailioConfigIP() {
    local NAME="$1"
    local VALUE="$2"
    local CONFIG_FILE="$3"

    sed -i -r -e "s|(#!substdef.*!$NAME!).*(!.*)|\1$VALUE\2|g" ${CONFIG_FILE}
}

# $1 == attribute name
# $2 == value of attribute
# $3 == rtpengine config file
setRtpengineConfigAttrib() {
    local NAME="$1"
    local VALUE="$2"
    local CONFIG_FILE="$3"

    sed -i -r -e "s|($NAME[[:space:]]?=[[:space:]]?.*)|$NAME = $VALUE|g" ${CONFIG_FILE}
}

# $1 == command to test
# returns: 0 == true, 1 == false
cmdExists() {
    if command -v "$1" > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# $1 == directory to check for in PATH
# returns: 0 == found, 1 == not found
pathCheck() {
    case ":${PATH-}:" in
        *:"$1":*)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# returns: AMI instance ID || blank string
getInstanceID() {
    curl http://169.254.169.254/latest/meta-data/instance-id 2>/dev/null ||
    ec2-metadata -i 2>/dev/null
}

# $1 == crontab entry to append
cronAppend() {
    local ENTRY="$1"
    crontab -l | { cat; echo "$ENTRY"; } | crontab -
}

# $1 == crontab entry to remove
cronRemove() {
    local ENTRY="$1"
    crontab -l | grep -v -F -w "$ENTRY" | crontab -
}
