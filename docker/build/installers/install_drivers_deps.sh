#!/usr/bin/env bash

###############################################################################
# Copyright 2020 The Apollo Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Fail on first error.
set -e
MY_MODE="$1"

cd "$(dirname "${BASH_SOURCE[0]}")"
. /tmp/installers/installer_base.sh

bash /tmp/installers/install_opencv.sh
bash /tmp/installers/install_adv_plat.sh "${MY_MODE}"
bash /tmp/installers/install_proj4.sh

# Required by python audio driver
apt_get_update_and_install \
    python3-pyaudio \
    portaudio19-dev

# Clean up cache to reduce layer size.
apt-get clean && \
    rm -rf /var/lib/apt/lists/*
