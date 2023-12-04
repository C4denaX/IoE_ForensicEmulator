#!/bin/bash
snmpget -v2c -c public $1 sysDescr.0
