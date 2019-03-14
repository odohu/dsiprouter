#!/usr/bin/env bash
#set -x
ENABLED=1 # ENABLED=1 --> install, ENABLED=0 --> do nothing, ENABLED=-1 uninstall

function installSQL {
    local TABLES=(dsip_multidomain_mapping dsip_domain_mapping)

    echo "Adding/Replacing the tables needed for Domain Mapping within dSIPRouter..."

    # Check to see if table exists
    mysql -s -N --user="$MYSQL_ROOT_USERNAME" --password="$MYSQL_ROOT_PASSWORD" $MYSQL_KAM_DATABASE -e "select count(*) from ${TABLES[0]} limit 1" > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo -e "The dSIPRouter tables ${TABLES[@]} already exists. Merging table data"
        (cat ${DSIP_PROJECT_DIR}/gui/modules/domain/domain_mapping.sql;
            mysqldump --single-transaction --skip-triggers --skip-add-drop-table --no-create-info --insert-ignore \
                --user="$MYSQL_KAM_USERNAME" --password="$MYSQL_KAM_PASSWORD" ${MYSQL_KAM_DATABASE} ${TABLES[@]};
        ) | mysql --user="$MYSQL_ROOT_USERNAME" --password="$MYSQL_ROOT_PASSWORD" $MYSQL_KAM_DATABASE
    else
        echo -e "Installing schema for Domain Mapping"
        mysql -sN --user="$MYSQL_ROOT_USERNAME" --password="$MYSQL_ROOT_PASSWORD" $MYSQL_KAM_DATABASE \
            < ${DSIP_PROJECT_DIR}/gui/modules/domain/domain_mapping.sql
    fi
}

function install {
    installSQL
    echo "Domain module installed"
}

function uninstall {
    echo "Domain module uninstalled"
}

function main {
    if [[ ${ENABLED} -eq 1 ]]; then
        install
    elif [[ ${ENABLED} -eq -1 ]]; then
        uninstall
    else
        exit 0
    fi
}

main
