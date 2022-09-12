# coding: utf8
#
# Copyright 2022 by Delphix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This class has been automatically generated from:
#     /delphix-schedule-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.Policy import Policy
from delphixpy.v1_6_0 import factory
from delphixpy.v1_6_0 import common

class __Undef(object):
    def __repr__(self):
        return "undef"

    def __setattr__(self, name, value):
        raise Exception('Cannot modify attributes of __Undef.')

_UNDEFINED = __Undef()

try:
    TEXT_TYPE = unicode
except NameError:
    TEXT_TYPE = str

class SchedulePolicy(Policy):
    """
    *(extends* :py:class:`v1_6_0.web.vo.Policy` *)* The base type for all
    schedule policies.
    """
    def __init__(self, undef_enabled=True):
        super(SchedulePolicy, self).__init__()
        self._type = ("SchedulePolicy", True)
        self._schedule_list = (self.__undef__, True)
        self._timezone = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SchedulePolicy, cls).from_dict(data, dirty, undef_enabled)
        obj._schedule_list = []
        for item in data.get("scheduleList") or []:
            obj._schedule_list.append(factory.create_object(item))
            factory.validate_type(obj._schedule_list[-1], "Schedule")
        obj._schedule_list = (obj._schedule_list, dirty)
        obj._timezone = (data.get("timezone", obj.__undef__), dirty)
        if obj._timezone[0] is not None and obj._timezone[0] is not obj.__undef__:
            assert isinstance(obj._timezone[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._timezone[0], type(obj._timezone[0])))
            assert obj._timezone[0] in ['ACT', 'AET', 'AGT', 'ART', 'AST', 'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'BET', 'BST', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CAT', 'CET', 'CNT', 'CST', 'CST6CDT', 'CTT', 'Canada/Atlantic', 'Canada/Central', 'Canada/East-Saskatchewan', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EAT', 'ECT', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'IET', 'IST', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'JST', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MIT', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NET', 'NST', 'NZ', 'NZ-CHAT', 'Navajo', 'PLT', 'PNT', 'PRC', 'PRT', 'PST', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROK', 'SST', 'Singapore', 'SystemV/AST4', 'SystemV/AST4ADT', 'SystemV/CST6', 'SystemV/CST6CDT', 'SystemV/EST5', 'SystemV/EST5EDT', 'SystemV/HST10', 'SystemV/MST7', 'SystemV/MST7MDT', 'SystemV/PST8', 'SystemV/PST8PDT', 'SystemV/YST9', 'SystemV/YST9YDT', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'VST', 'W-SU', 'WET', 'Zulu'], "Expected enum ['ACT', 'AET', 'AGT', 'ART', 'AST', 'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'BET', 'BST', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CAT', 'CET', 'CNT', 'CST', 'CST6CDT', 'CTT', 'Canada/Atlantic', 'Canada/Central', 'Canada/East-Saskatchewan', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EAT', 'ECT', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'IET', 'IST', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'JST', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MIT', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NET', 'NST', 'NZ', 'NZ-CHAT', 'Navajo', 'PLT', 'PNT', 'PRC', 'PRT', 'PST', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROK', 'SST', 'Singapore', 'SystemV/AST4', 'SystemV/AST4ADT', 'SystemV/CST6', 'SystemV/CST6CDT', 'SystemV/EST5', 'SystemV/EST5EDT', 'SystemV/HST10', 'SystemV/MST7', 'SystemV/MST7MDT', 'SystemV/PST8', 'SystemV/PST8PDT', 'SystemV/YST9', 'SystemV/YST9YDT', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'VST', 'W-SU', 'WET', 'Zulu'] but got %s" % obj._timezone[0]
            common.validate_format(obj._timezone[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SchedulePolicy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "schedule_list" == "type" or (self.schedule_list is not self.__undef__ and (not (dirty and not self._schedule_list[1]) or isinstance(self.schedule_list, list) or belongs_to_parent)):
            dct["scheduleList"] = dictify(self.schedule_list, prop_is_list_or_vo=True)
        if "timezone" == "type" or (self.timezone is not self.__undef__ and (not (dirty and not self._timezone[1]) or isinstance(self.timezone, list) or belongs_to_parent)):
            dct["timezone"] = dictify(self.timezone)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._schedule_list = (self._schedule_list[0], True)
        self._timezone = (self._timezone[0], True)

    def is_dirty(self):
        return any([self._schedule_list[1], self._timezone[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SchedulePolicy):
            return False
        return super(SchedulePolicy, self).__eq__(other) and \
               self.schedule_list == other.schedule_list and \
               self.timezone == other.timezone

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def schedule_list(self):
        """
        List of Schedule objects representing when the policy will execute.

        :rtype: ``list`` of :py:class:`v1_6_0.web.vo.Schedule`
        """
        return self._schedule_list[0]

    @schedule_list.setter
    def schedule_list(self, value):
        self._schedule_list = (value, True)

    @property
    def timezone(self):
        """
        The timezone of this policy. *(permitted values: ACT, AET, AGT, ART,
        AST, Africa/Abidjan, Africa/Accra, Africa/Addis_Ababa, Africa/Algiers,
        Africa/Asmara, Africa/Asmera, Africa/Bamako, Africa/Bangui,
        Africa/Banjul, Africa/Bissau, Africa/Blantyre, Africa/Brazzaville,
        Africa/Bujumbura, Africa/Cairo, Africa/Casablanca, Africa/Ceuta,
        Africa/Conakry, Africa/Dakar, Africa/Dar_es_Salaam, Africa/Djibouti,
        Africa/Douala, Africa/El_Aaiun, Africa/Freetown, Africa/Gaborone,
        Africa/Harare, Africa/Johannesburg, Africa/Juba, Africa/Kampala,
        Africa/Khartoum, Africa/Kigali, Africa/Kinshasa, Africa/Lagos,
        Africa/Libreville, Africa/Lome, Africa/Luanda, Africa/Lubumbashi,
        Africa/Lusaka, Africa/Malabo, Africa/Maputo, Africa/Maseru,
        Africa/Mbabane, Africa/Mogadishu, Africa/Monrovia, Africa/Nairobi,
        Africa/Ndjamena, Africa/Niamey, Africa/Nouakchott, Africa/Ouagadougou,
        Africa/Porto-Novo, Africa/Sao_Tome, Africa/Timbuktu, Africa/Tripoli,
        Africa/Tunis, Africa/Windhoek, America/Adak, America/Anchorage,
        America/Anguilla, America/Antigua, America/Araguaina,
        America/Argentina/Buenos_Aires, America/Argentina/Catamarca,
        America/Argentina/ComodRivadavia, America/Argentina/Cordoba,
        America/Argentina/Jujuy, America/Argentina/La_Rioja,
        America/Argentina/Mendoza, America/Argentina/Rio_Gallegos,
        America/Argentina/Salta, America/Argentina/San_Juan,
        America/Argentina/San_Luis, America/Argentina/Tucuman,
        America/Argentina/Ushuaia, America/Aruba, America/Asuncion,
        America/Atikokan, America/Atka, America/Bahia, America/Bahia_Banderas,
        America/Barbados, America/Belem, America/Belize, America/Blanc-Sablon,
        America/Boa_Vista, America/Bogota, America/Boise, America/Buenos_Aires,
        America/Cambridge_Bay, America/Campo_Grande, America/Cancun,
        America/Caracas, America/Catamarca, America/Cayenne, America/Cayman,
        America/Chicago, America/Chihuahua, America/Coral_Harbour,
        America/Cordoba, America/Costa_Rica, America/Creston, America/Cuiaba,
        America/Curacao, America/Danmarkshavn, America/Dawson,
        America/Dawson_Creek, America/Denver, America/Detroit,
        America/Dominica, America/Edmonton, America/Eirunepe,
        America/El_Salvador, America/Ensenada, America/Fort_Wayne,
        America/Fortaleza, America/Glace_Bay, America/Godthab,
        America/Goose_Bay, America/Grand_Turk, America/Grenada,
        America/Guadeloupe, America/Guatemala, America/Guayaquil,
        America/Guyana, America/Halifax, America/Havana, America/Hermosillo,
        America/Indiana/Indianapolis, America/Indiana/Knox,
        America/Indiana/Marengo, America/Indiana/Petersburg,
        America/Indiana/Tell_City, America/Indiana/Vevay,
        America/Indiana/Vincennes, America/Indiana/Winamac,
        America/Indianapolis, America/Inuvik, America/Iqaluit, America/Jamaica,
        America/Jujuy, America/Juneau, America/Kentucky/Louisville,
        America/Kentucky/Monticello, America/Knox_IN, America/Kralendijk,
        America/La_Paz, America/Lima, America/Los_Angeles, America/Louisville,
        America/Lower_Princes, America/Maceio, America/Managua, America/Manaus,
        America/Marigot, America/Martinique, America/Matamoros,
        America/Mazatlan, America/Mendoza, America/Menominee, America/Merida,
        America/Metlakatla, America/Mexico_City, America/Miquelon,
        America/Moncton, America/Monterrey, America/Montevideo,
        America/Montreal, America/Montserrat, America/Nassau, America/New_York,
        America/Nipigon, America/Nome, America/Noronha,
        America/North_Dakota/Beulah, America/North_Dakota/Center,
        America/North_Dakota/New_Salem, America/Ojinaga, America/Panama,
        America/Pangnirtung, America/Paramaribo, America/Phoenix, America/Port-
        au-Prince, America/Port_of_Spain, America/Porto_Acre,
        America/Porto_Velho, America/Puerto_Rico, America/Rainy_River,
        America/Rankin_Inlet, America/Recife, America/Regina, America/Resolute,
        America/Rio_Branco, America/Rosario, America/Santa_Isabel,
        America/Santarem, America/Santiago, America/Santo_Domingo,
        America/Sao_Paulo, America/Scoresbysund, America/Shiprock,
        America/Sitka, America/St_Barthelemy, America/St_Johns,
        America/St_Kitts, America/St_Lucia, America/St_Thomas,
        America/St_Vincent, America/Swift_Current, America/Tegucigalpa,
        America/Thule, America/Thunder_Bay, America/Tijuana, America/Toronto,
        America/Tortola, America/Vancouver, America/Virgin, America/Whitehorse,
        America/Winnipeg, America/Yakutat, America/Yellowknife,
        Antarctica/Casey, Antarctica/Davis, Antarctica/DumontDUrville,
        Antarctica/Macquarie, Antarctica/Mawson, Antarctica/McMurdo,
        Antarctica/Palmer, Antarctica/Rothera, Antarctica/South_Pole,
        Antarctica/Syowa, Antarctica/Troll, Antarctica/Vostok,
        Arctic/Longyearbyen, Asia/Aden, Asia/Almaty, Asia/Amman, Asia/Anadyr,
        Asia/Aqtau, Asia/Aqtobe, Asia/Ashgabat, Asia/Ashkhabad, Asia/Baghdad,
        Asia/Bahrain, Asia/Baku, Asia/Bangkok, Asia/Beirut, Asia/Bishkek,
        Asia/Brunei, Asia/Calcutta, Asia/Chita, Asia/Choibalsan,
        Asia/Chongqing, Asia/Chungking, Asia/Colombo, Asia/Dacca,
        Asia/Damascus, Asia/Dhaka, Asia/Dili, Asia/Dubai, Asia/Dushanbe,
        Asia/Gaza, Asia/Harbin, Asia/Hebron, Asia/Ho_Chi_Minh, Asia/Hong_Kong,
        Asia/Hovd, Asia/Irkutsk, Asia/Istanbul, Asia/Jakarta, Asia/Jayapura,
        Asia/Jerusalem, Asia/Kabul, Asia/Kamchatka, Asia/Karachi, Asia/Kashgar,
        Asia/Kathmandu, Asia/Katmandu, Asia/Khandyga, Asia/Kolkata,
        Asia/Krasnoyarsk, Asia/Kuala_Lumpur, Asia/Kuching, Asia/Kuwait,
        Asia/Macao, Asia/Macau, Asia/Magadan, Asia/Makassar, Asia/Manila,
        Asia/Muscat, Asia/Nicosia, Asia/Novokuznetsk, Asia/Novosibirsk,
        Asia/Omsk, Asia/Oral, Asia/Phnom_Penh, Asia/Pontianak, Asia/Pyongyang,
        Asia/Qatar, Asia/Qyzylorda, Asia/Rangoon, Asia/Riyadh, Asia/Saigon,
        Asia/Sakhalin, Asia/Samarkand, Asia/Seoul, Asia/Shanghai,
        Asia/Singapore, Asia/Srednekolymsk, Asia/Taipei, Asia/Tashkent,
        Asia/Tbilisi, Asia/Tehran, Asia/Tel_Aviv, Asia/Thimbu, Asia/Thimphu,
        Asia/Tokyo, Asia/Ujung_Pandang, Asia/Ulaanbaatar, Asia/Ulan_Bator,
        Asia/Urumqi, Asia/Ust-Nera, Asia/Vientiane, Asia/Vladivostok,
        Asia/Yakutsk, Asia/Yekaterinburg, Asia/Yerevan, Atlantic/Azores,
        Atlantic/Bermuda, Atlantic/Canary, Atlantic/Cape_Verde,
        Atlantic/Faeroe, Atlantic/Faroe, Atlantic/Jan_Mayen, Atlantic/Madeira,
        Atlantic/Reykjavik, Atlantic/South_Georgia, Atlantic/St_Helena,
        Atlantic/Stanley, Australia/ACT, Australia/Adelaide,
        Australia/Brisbane, Australia/Broken_Hill, Australia/Canberra,
        Australia/Currie, Australia/Darwin, Australia/Eucla, Australia/Hobart,
        Australia/LHI, Australia/Lindeman, Australia/Lord_Howe,
        Australia/Melbourne, Australia/NSW, Australia/North, Australia/Perth,
        Australia/Queensland, Australia/South, Australia/Sydney,
        Australia/Tasmania, Australia/Victoria, Australia/West,
        Australia/Yancowinna, BET, BST, Brazil/Acre, Brazil/DeNoronha,
        Brazil/East, Brazil/West, CAT, CET, CNT, CST, CST6CDT, CTT,
        Canada/Atlantic, Canada/Central, Canada/East-Saskatchewan,
        Canada/Eastern, Canada/Mountain, Canada/Newfoundland, Canada/Pacific,
        Canada/Saskatchewan, Canada/Yukon, Chile/Continental,
        Chile/EasterIsland, Cuba, EAT, ECT, EET, EST, EST5EDT, Egypt, Eire,
        Etc/GMT, Etc/GMT+0, Etc/GMT+1, Etc/GMT+10, Etc/GMT+11, Etc/GMT+12,
        Etc/GMT+2, Etc/GMT+3, Etc/GMT+4, Etc/GMT+5, Etc/GMT+6, Etc/GMT+7,
        Etc/GMT+8, Etc/GMT+9, Etc/GMT-0, Etc/GMT-1, Etc/GMT-10, Etc/GMT-11,
        Etc/GMT-12, Etc/GMT-13, Etc/GMT-14, Etc/GMT-2, Etc/GMT-3, Etc/GMT-4,
        Etc/GMT-5, Etc/GMT-6, Etc/GMT-7, Etc/GMT-8, Etc/GMT-9, Etc/GMT0,
        Etc/Greenwich, Etc/UCT, Etc/UTC, Etc/Universal, Etc/Zulu,
        Europe/Amsterdam, Europe/Andorra, Europe/Athens, Europe/Belfast,
        Europe/Belgrade, Europe/Berlin, Europe/Bratislava, Europe/Brussels,
        Europe/Bucharest, Europe/Budapest, Europe/Busingen, Europe/Chisinau,
        Europe/Copenhagen, Europe/Dublin, Europe/Gibraltar, Europe/Guernsey,
        Europe/Helsinki, Europe/Isle_of_Man, Europe/Istanbul, Europe/Jersey,
        Europe/Kaliningrad, Europe/Kiev, Europe/Lisbon, Europe/Ljubljana,
        Europe/London, Europe/Luxembourg, Europe/Madrid, Europe/Malta,
        Europe/Mariehamn, Europe/Minsk, Europe/Monaco, Europe/Moscow,
        Europe/Nicosia, Europe/Oslo, Europe/Paris, Europe/Podgorica,
        Europe/Prague, Europe/Riga, Europe/Rome, Europe/Samara,
        Europe/San_Marino, Europe/Sarajevo, Europe/Simferopol, Europe/Skopje,
        Europe/Sofia, Europe/Stockholm, Europe/Tallinn, Europe/Tirane,
        Europe/Tiraspol, Europe/Uzhgorod, Europe/Vaduz, Europe/Vatican,
        Europe/Vienna, Europe/Vilnius, Europe/Volgograd, Europe/Warsaw,
        Europe/Zagreb, Europe/Zaporozhye, Europe/Zurich, GB, GB-Eire, GMT,
        GMT0, Greenwich, HST, Hongkong, IET, IST, Iceland, Indian/Antananarivo,
        Indian/Chagos, Indian/Christmas, Indian/Cocos, Indian/Comoro,
        Indian/Kerguelen, Indian/Mahe, Indian/Maldives, Indian/Mauritius,
        Indian/Mayotte, Indian/Reunion, Iran, Israel, JST, Jamaica, Japan,
        Kwajalein, Libya, MET, MIT, MST, MST7MDT, Mexico/BajaNorte,
        Mexico/BajaSur, Mexico/General, NET, NST, NZ, NZ-CHAT, Navajo, PLT,
        PNT, PRC, PRT, PST, PST8PDT, Pacific/Apia, Pacific/Auckland,
        Pacific/Bougainville, Pacific/Chatham, Pacific/Chuuk, Pacific/Easter,
        Pacific/Efate, Pacific/Enderbury, Pacific/Fakaofo, Pacific/Fiji,
        Pacific/Funafuti, Pacific/Galapagos, Pacific/Gambier,
        Pacific/Guadalcanal, Pacific/Guam, Pacific/Honolulu, Pacific/Johnston,
        Pacific/Kiritimati, Pacific/Kosrae, Pacific/Kwajalein, Pacific/Majuro,
        Pacific/Marquesas, Pacific/Midway, Pacific/Nauru, Pacific/Niue,
        Pacific/Norfolk, Pacific/Noumea, Pacific/Pago_Pago, Pacific/Palau,
        Pacific/Pitcairn, Pacific/Pohnpei, Pacific/Ponape,
        Pacific/Port_Moresby, Pacific/Rarotonga, Pacific/Saipan, Pacific/Samoa,
        Pacific/Tahiti, Pacific/Tarawa, Pacific/Tongatapu, Pacific/Truk,
        Pacific/Wake, Pacific/Wallis, Pacific/Yap, Poland, Portugal, ROK, SST,
        Singapore, SystemV/AST4, SystemV/AST4ADT, SystemV/CST6,
        SystemV/CST6CDT, SystemV/EST5, SystemV/EST5EDT, SystemV/HST10,
        SystemV/MST7, SystemV/MST7MDT, SystemV/PST8, SystemV/PST8PDT,
        SystemV/YST9, SystemV/YST9YDT, Turkey, UCT, US/Alaska, US/Aleutian,
        US/Arizona, US/Central, US/East-Indiana, US/Eastern, US/Hawaii,
        US/Indiana-Starke, US/Michigan, US/Mountain, US/Pacific, US/Pacific-
        New, US/Samoa, UTC, Universal, VST, W-SU, WET, Zulu)*

        :rtype: ``TEXT_TYPE``
        """
        return self._timezone[0]

    @timezone.setter
    def timezone(self, value):
        self._timezone = (value, True)

