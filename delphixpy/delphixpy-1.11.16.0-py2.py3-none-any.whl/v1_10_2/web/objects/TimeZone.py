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
#     /delphix-timezone.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_2 import common

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

class TimeZone(TypedObject):
    """
    *(extends* :py:class:`v1_10_2.web.vo.TypedObject` *)* This represents a
    time zone offset.
    """
    def __init__(self, undef_enabled=True):
        super(TimeZone, self).__init__()
        self._type = ("TimeZone", True)
        self._id = (self.__undef__, True)
        self._offset = (self.__undef__, True)
        self._offset_string = (self.__undef__, True)

    API_VERSION = "1.10.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TimeZone, cls).from_dict(data, dirty, undef_enabled)
        if "id" not in data:
            raise ValueError("Missing required property \"id\".")
        obj._id = (data.get("id", obj.__undef__), dirty)
        if obj._id[0] is not None and obj._id[0] is not obj.__undef__:
            assert isinstance(obj._id[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._id[0], type(obj._id[0])))
            assert obj._id[0] in ['ACT', 'AET', 'AGT', 'ART', 'AST', 'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tomsk', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'BET', 'BST', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CAT', 'CET', 'CNT', 'CST', 'CST6CDT', 'CTT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EAT', 'ECT', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'IET', 'IST', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'JST', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MIT', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NET', 'NST', 'NZ', 'NZ-CHAT', 'Navajo', 'PLT', 'PNT', 'PRC', 'PRT', 'PST', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROK', 'SST', 'Singapore', 'SystemV/AST4', 'SystemV/AST4ADT', 'SystemV/CST6', 'SystemV/CST6CDT', 'SystemV/EST5', 'SystemV/EST5EDT', 'SystemV/HST10', 'SystemV/MST7', 'SystemV/MST7MDT', 'SystemV/PST8', 'SystemV/PST8PDT', 'SystemV/YST9', 'SystemV/YST9YDT', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'VST', 'W-SU', 'WET', 'Zulu'], "Expected enum ['ACT', 'AET', 'AGT', 'ART', 'AST', 'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tomsk', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'BET', 'BST', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CAT', 'CET', 'CNT', 'CST', 'CST6CDT', 'CTT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EAT', 'ECT', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'IET', 'IST', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'JST', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MIT', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NET', 'NST', 'NZ', 'NZ-CHAT', 'Navajo', 'PLT', 'PNT', 'PRC', 'PRT', 'PST', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROK', 'SST', 'Singapore', 'SystemV/AST4', 'SystemV/AST4ADT', 'SystemV/CST6', 'SystemV/CST6CDT', 'SystemV/EST5', 'SystemV/EST5EDT', 'SystemV/HST10', 'SystemV/MST7', 'SystemV/MST7MDT', 'SystemV/PST8', 'SystemV/PST8PDT', 'SystemV/YST9', 'SystemV/YST9YDT', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'VST', 'W-SU', 'WET', 'Zulu'] but got %s" % obj._id[0]
            common.validate_format(obj._id[0], "None", None, None)
        obj._offset = (data.get("offset", obj.__undef__), dirty)
        if obj._offset[0] is not None and obj._offset[0] is not obj.__undef__:
            assert isinstance(obj._offset[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._offset[0], type(obj._offset[0])))
            common.validate_format(obj._offset[0], "None", None, None)
        obj._offset_string = (data.get("offsetString", obj.__undef__), dirty)
        if obj._offset_string[0] is not None and obj._offset_string[0] is not obj.__undef__:
            assert isinstance(obj._offset_string[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._offset_string[0], type(obj._offset_string[0])))
            common.validate_format(obj._offset_string[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TimeZone, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "id" == "type" or (self.id is not self.__undef__ and (not (dirty and not self._id[1]) or isinstance(self.id, list) or belongs_to_parent)):
            dct["id"] = dictify(self.id)
        if "offset" == "type" or (self.offset is not self.__undef__ and (not (dirty and not self._offset[1]))):
            dct["offset"] = dictify(self.offset)
        if "offset_string" == "type" or (self.offset_string is not self.__undef__ and (not (dirty and not self._offset_string[1]))):
            dct["offsetString"] = dictify(self.offset_string)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._id = (self._id[0], True)
        self._offset = (self._offset[0], True)
        self._offset_string = (self._offset_string[0], True)

    def is_dirty(self):
        return any([self._id[1], self._offset[1], self._offset_string[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TimeZone):
            return False
        return super(TimeZone, self).__eq__(other) and \
               self.id == other.id and \
               self.offset == other.offset and \
               self.offset_string == other.offset_string

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def id(self):
        """
        The ID of this time zone. *(permitted values: ACT, AET, AGT, ART, AST,
        Africa/Abidjan, Africa/Accra, Africa/Addis_Ababa, Africa/Algiers,
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
        America/El_Salvador, America/Ensenada, America/Fort_Nelson,
        America/Fort_Wayne, America/Fortaleza, America/Glace_Bay,
        America/Godthab, America/Goose_Bay, America/Grand_Turk,
        America/Grenada, America/Guadeloupe, America/Guatemala,
        America/Guayaquil, America/Guyana, America/Halifax, America/Havana,
        America/Hermosillo, America/Indiana/Indianapolis, America/Indiana/Knox,
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
        America/Porto_Velho, America/Puerto_Rico, America/Punta_Arenas,
        America/Rainy_River, America/Rankin_Inlet, America/Recife,
        America/Regina, America/Resolute, America/Rio_Branco, America/Rosario,
        America/Santa_Isabel, America/Santarem, America/Santiago,
        America/Santo_Domingo, America/Sao_Paulo, America/Scoresbysund,
        America/Shiprock, America/Sitka, America/St_Barthelemy,
        America/St_Johns, America/St_Kitts, America/St_Lucia,
        America/St_Thomas, America/St_Vincent, America/Swift_Current,
        America/Tegucigalpa, America/Thule, America/Thunder_Bay,
        America/Tijuana, America/Toronto, America/Tortola, America/Vancouver,
        America/Virgin, America/Whitehorse, America/Winnipeg, America/Yakutat,
        America/Yellowknife, Antarctica/Casey, Antarctica/Davis,
        Antarctica/DumontDUrville, Antarctica/Macquarie, Antarctica/Mawson,
        Antarctica/McMurdo, Antarctica/Palmer, Antarctica/Rothera,
        Antarctica/South_Pole, Antarctica/Syowa, Antarctica/Troll,
        Antarctica/Vostok, Arctic/Longyearbyen, Asia/Aden, Asia/Almaty,
        Asia/Amman, Asia/Anadyr, Asia/Aqtau, Asia/Aqtobe, Asia/Ashgabat,
        Asia/Ashkhabad, Asia/Atyrau, Asia/Baghdad, Asia/Bahrain, Asia/Baku,
        Asia/Bangkok, Asia/Barnaul, Asia/Beirut, Asia/Bishkek, Asia/Brunei,
        Asia/Calcutta, Asia/Chita, Asia/Choibalsan, Asia/Chongqing,
        Asia/Chungking, Asia/Colombo, Asia/Dacca, Asia/Damascus, Asia/Dhaka,
        Asia/Dili, Asia/Dubai, Asia/Dushanbe, Asia/Famagusta, Asia/Gaza,
        Asia/Harbin, Asia/Hebron, Asia/Ho_Chi_Minh, Asia/Hong_Kong, Asia/Hovd,
        Asia/Irkutsk, Asia/Istanbul, Asia/Jakarta, Asia/Jayapura,
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
        Asia/Tomsk, Asia/Tokyo, Asia/Ujung_Pandang, Asia/Ulaanbaatar,
        Asia/Ulan_Bator, Asia/Urumqi, Asia/Ust-Nera, Asia/Vientiane,
        Asia/Vladivostok, Asia/Yakutsk, Asia/Yangon, Asia/Yekaterinburg,
        Asia/Yerevan, Atlantic/Azores, Atlantic/Bermuda, Atlantic/Canary,
        Atlantic/Cape_Verde, Atlantic/Faeroe, Atlantic/Faroe,
        Atlantic/Jan_Mayen, Atlantic/Madeira, Atlantic/Reykjavik,
        Atlantic/South_Georgia, Atlantic/St_Helena, Atlantic/Stanley,
        Australia/ACT, Australia/Adelaide, Australia/Brisbane,
        Australia/Broken_Hill, Australia/Canberra, Australia/Currie,
        Australia/Darwin, Australia/Eucla, Australia/Hobart, Australia/LHI,
        Australia/Lindeman, Australia/Lord_Howe, Australia/Melbourne,
        Australia/NSW, Australia/North, Australia/Perth, Australia/Queensland,
        Australia/South, Australia/Sydney, Australia/Tasmania,
        Australia/Victoria, Australia/West, Australia/Yancowinna, BET, BST,
        Brazil/Acre, Brazil/DeNoronha, Brazil/East, Brazil/West, CAT, CET, CNT,
        CST, CST6CDT, CTT, Canada/Atlantic, Canada/Central, Canada/Eastern,
        Canada/Mountain, Canada/Newfoundland, Canada/Pacific,
        Canada/Saskatchewan, Canada/Yukon, Chile/Continental,
        Chile/EasterIsland, Cuba, EAT, ECT, EET, EST, EST5EDT, Egypt, Eire,
        Etc/GMT, Etc/GMT+0, Etc/GMT+1, Etc/GMT+10, Etc/GMT+11, Etc/GMT+12,
        Etc/GMT+2, Etc/GMT+3, Etc/GMT+4, Etc/GMT+5, Etc/GMT+6, Etc/GMT+7,
        Etc/GMT+8, Etc/GMT+9, Etc/GMT-0, Etc/GMT-1, Etc/GMT-10, Etc/GMT-11,
        Etc/GMT-12, Etc/GMT-13, Etc/GMT-14, Etc/GMT-2, Etc/GMT-3, Etc/GMT-4,
        Etc/GMT-5, Etc/GMT-6, Etc/GMT-7, Etc/GMT-8, Etc/GMT-9, Etc/GMT0,
        Etc/Greenwich, Etc/UCT, Etc/UTC, Etc/Universal, Etc/Zulu,
        Europe/Amsterdam, Europe/Andorra, Europe/Astrakhan, Europe/Athens,
        Europe/Belfast, Europe/Belgrade, Europe/Berlin, Europe/Bratislava,
        Europe/Brussels, Europe/Bucharest, Europe/Budapest, Europe/Busingen,
        Europe/Chisinau, Europe/Copenhagen, Europe/Dublin, Europe/Gibraltar,
        Europe/Guernsey, Europe/Helsinki, Europe/Isle_of_Man, Europe/Istanbul,
        Europe/Jersey, Europe/Kaliningrad, Europe/Kiev, Europe/Kirov,
        Europe/Lisbon, Europe/Ljubljana, Europe/London, Europe/Luxembourg,
        Europe/Madrid, Europe/Malta, Europe/Mariehamn, Europe/Minsk,
        Europe/Monaco, Europe/Moscow, Europe/Nicosia, Europe/Oslo,
        Europe/Paris, Europe/Podgorica, Europe/Prague, Europe/Riga,
        Europe/Rome, Europe/Samara, Europe/San_Marino, Europe/Sarajevo,
        Europe/Saratov, Europe/Simferopol, Europe/Skopje, Europe/Sofia,
        Europe/Stockholm, Europe/Tallinn, Europe/Tirane, Europe/Tiraspol,
        Europe/Ulyanovsk, Europe/Uzhgorod, Europe/Vaduz, Europe/Vatican,
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
        return self._id[0]

    @id.setter
    def id(self, value):
        self._id = (value, True)

    @property
    def offset(self):
        """
        The difference, in minutes, between UTC and local time. For example, if
        your time zone is UTC -5:00 (Eastern Standard Time), 300 will be
        returned. Daylight saving time prevents this value from being a
        constant even for a given locale.

        :rtype: ``int``
        """
        return self._offset[0]

    @offset.setter
    def offset(self, value):
        self._offset = (value, True)

    @property
    def offset_string(self):
        """
        The Offset as a String. For instance 'UTC -5:00'.

        :rtype: ``TEXT_TYPE``
        """
        return self._offset_string[0]

    @offset_string.setter
    def offset_string(self, value):
        self._offset_string = (value, True)

