#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask

from geo import geo
from routes import Routes


blueprints = (
    (geo.create_blueprint(), '/services/geo'),)

base_routes = Routes()


class Eclipse2017GeoApp(Flask):
    """
    Eclipse 2017 application.
    """
    def __init__(
            self, project_id, session_enc_key, google_oauth2_client_id,
            google_oauth2_client_secret, debug=False,
            blueprints=blueprints, routes=base_routes, geo=geo,
            **kwargs):
        super(Eclipse2017GeoApp, self).__init__(__name__, **kwargs)

        self.config['PROJECT_ID'] = project_id
        self.config['SECRET_KEY'] = session_enc_key
        self.config['GOOGLE_OAUTH2_CLIENT_ID'] = google_oauth2_client_id
        self.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = google_oauth2_client_secret


        self.geo = geo

        self.debug = debug
        routes.register(self, blueprints)
