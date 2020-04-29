import pymongo

#database connection
client = pymongo.MongoClient("mongodb+srv://chitrank_0614:chitrank0614@smartirrigation-scp4o.mongodb.net/test?retryWrites=true&w=majority")
database=client.get_database("SmartIrrigation")

#collection connections
crops=database.Crops
grass=database.Grass
rice=database.Rice
wheat=database.Wheat
weather_codes=database.WeatherCodes
city_codes=database.CityCodes




# city_codes database

# res = city_codes.insert_many([{"City": "greater noida", "Code": 6954929},
#                               {"City": "noida", "Code": 7279746},
#                               {"City": "new delhi", "Code": 1261481},
#                               {"City": "chandigarh", "Code": 1274746},
#                               {"City": "srinagar", "Code": 1255634},
#                               {"City": "gurgaon", "Code": 1270642},
#                               {"City": "lucknow", "Code": 1264733},
#                               {"City": "ludhiana", "Code": 1264728},
#                               {"City": "meerut", "Code": 1263214},
#                               {"City": "jhansi", "Code": 1269006},
#                               {"City": "kanpur", "Code": 1267995},
#                               {"City": "agra", "Code": 1269564},
#                               {"City": "gwalior", "Code": 1270583},
#                               {"City": "mumbai", "Code": 1275339},
#                               {"City": "calcutta", "Code": 1275004},
#                               {"City": "chennai", "Code": 1264527},
#                               {"City": "pune", "Code": 1259229},
#                               {"City": "bhopal", "Code": 1275841},
#                               {"City": "jabalpur", "Code": 1269633},
#                               {"City": "sagar", "Code": 1257845},
#                               {"City": "ranchi", "Code": 1258526},
#                               {"City": "patna", "Code": 1260082},
#                               {"City": "puri", "Code": 1259184},
#                               {"City": "hyderabad", "Code": 1269843},
#                               {"City": "bangalore", "Code": 1277333},
#                               {"City": "kochi", "Code": 1273874},
#                               {"City": "nagpur", "Code": 1262180},
#                               {"City": "jaipur", "Code": 1269515},
#                               {"City": "jodhpur", "Code": 1268865},
#                               {"City": "shillong", "Code": 1256523},
#                               {"City": "guwahati", "Code": 1261186},
#                               {"City": "london", "Code": 2643743}
#                               ])
# # print(res.inserted_ids)


# weather_Codes entry

# res=weather_Codes.insert_many([ { "Code" : 200, "Class" : "Thunderstorm", "Detail" : "thunderstorm with light rain" },
#                                 { "Code" : 201, "Class" : "Thunderstorm", "Detail" : "thunderstorm with rain" },
#                                 { "Code" : 202, "Class" : "Thunderstorm", "Detail" : "thunderstorm with heavy rain" },
#                                 { "Code" : 210, "Class" : "Thunderstorm", "Detail" : "light thunderstorm" },
#                                 { "Code" : 211, "Class" : "Thunderstorm", "Detail" : "thunderstorm" },
#                                 { "Code" : 212, "Class" : "Thunderstorm", "Detail" : "heavy thunderstorm" },
#                                 { "Code" : 221, "Class" : "Thunderstorm", "Detail" : "ragged thunderstorm" },
#                                 { "Code" : 230, "Class" : "Thunderstorm", "Detail" : "thunderstorm with light drizzle" },
#                                 { "Code" : 231, "Class" : "Thunderstorm", "Detail" : "thunderstorm with drizzle" },
#                                 { "Code" : 232, "Class" : "Thunderstorm", "Detail" : "thunderstorm with heavy drizzle" },
#                                 { "Code" : 300, "Class" : "Drizzle", "Detail" : "light intensity drizzle" },
#                                 { "Code" : 301, "Class" : "Drizzle", "Detail" : "drizzle" },
#                                 { "Code" : 302, "Class" : "Drizzle", "Detail" : "heavy intensity drizzle" },
#                                 { "Code" : 310, "Class" : "Drizzle", "Detail" : "light intensity drizzle rain" },
#                                 { "Code" : 311, "Class" : "Drizzle", "Detail" : "drizzle rain" },
#                                 { "Code" : 312, "Class" : "Drizzle", "Detail" : "heavy intensity drizzle rain" },
#                                 { "Code" : 313, "Class" : "Drizzle", "Detail" : "shower rain and drizzle" },
#                                 { "Code" : 314, "Class" : "Drizzle", "Detail" : "heavy shower rain and drizzle" },
#                                 { "Code" : 321, "Class" : "Drizzle", "Detail" : "shower drizzle" },
#                                 { "Code" : 500, "Class" : "Rain", "Detail" : "light rain" },
#                                 { "Code" : 501, "Class" : "Rain", "Detail" : "moderate rain" },
#                                 { "Code" : 502, "Class" : "Rain", "Detail" : "heavy intensity rain" },
#                                 { "Code" : 503, "Class" : "Rain", "Detail" : "very heavy rain" },
#                                 { "Code" : 504, "Class" : "Rain", "Detail" : "extreme rain" },
#                                 { "Code" : 511, "Class" : "Rain", "Detail" : "freezing rain" },
#                                 { "Code" : 520, "Class" : "Rain", "Detail" : "light intensity shower rain" },
#                                 { "Code" : 521, "Class" : "Rain", "Detail" : "shower rain" },
#                                 { "Code" : 522, "Class" : "Rain", "Detail" : "heavy intensity shower rain" },
#                                 { "Code" : 531, "Class" : "Rain", "Detail" : "ragged shower rain" },
#                                 { "Code" : 600, "Class" : "Snow", "Detail" : "light snow" },
#                                 { "Code" : 601, "Class" : "Snow", "Detail" : "Snow" },
#                                 { "Code" : 602, "Class" : "Snow", "Detail" : "Heavy snow" },
#                                 { "Code" : 611, "Class" : "Snow", "Detail" : "Sleet" },
#                                 { "Code" : 612, "Class" : "Snow", "Detail" : "Light shower sleet" },
#                                 { "Code" : 613, "Class" : "Snow", "Detail" : "Shower sleet" },
#                                 { "Code" : 615, "Class" : "Snow", "Detail" : "Light rain and snow" },
#                                 { "Code" : 616, "Class" : "Snow", "Detail" : "Rain and snow" },
#                                 { "Code" : 620, "Class" : "Snow", "Detail" : "Light shower snow" },
#                                 { "Code" : 621, "Class" : "Snow", "Detail" : "Shower snow" },
#                                 { "Code" : 622, "Class" : "Snow", "Detail" : "Heavy shower snow" },
#                                 { "Code" : 701, "Class" : "Mist", "Detail" : "mist" },
#                                 { "Code" : 711, "Class" : "Smoke", "Detail" : "Smoke" },
#                                 { "Code" : 721, "Class" : "Haze", "Detail" : "Haze" },
#                                 { "Code" : 731, "Class" : "Dust", "Detail" : "sand/ dust whirls" },
#                                 { "Code" : 741, "Class" : "Fog", "Detail" : "fog" },
#                                 { "Code" : 751, "Class" : "Sand", "Detail" : "sand" },
#                                 { "Code" : 761, "Class" : "Dust", "Detail" : "dust" },
#                                 { "Code" : 762, "Class" : "Ash", "Detail" : "volcanic ash" },
#                                 { "Code" : 771, "Class" : "Squall", "Detail" : "squalls" },
#                                 { "Code" : 781, "Class" : "Tornado", "Detail" : "tornado" },
#                                 { "Code" : 800, "Class" : "Clear", "Detail" : "clear sky" },
#                                 { "Code" : 801, "Class" : "Clouds", "Detail" : "few clouds: 11-25%" },
#                                 { "Code" : 802, "Class" : "Clouds", "Detail" : "scattered clouds: 25-50%" },
#                                 { "Code" : 803, "Class" : "Clouds", "Detail" : "broken clouds: 51-84%" },
#                                 { "Code" : 804, "Class" : "Clouds", "Detail" : "overcast clouds: 85-100%" }
#                                 ])
# # print(res.inserted_ids)

# wheat database entry

# res = wheat.insert_many([{"PeriodStart": 0, "PeriodEnd": 10080,
#                              "MinHeight": 0.5, "MaxHeight": 0.7},
#                          {"PeriodStart": 10081, "PeriodEnd": 20161,
#                              "MinHeight": 0.5, "MaxHeight": 0.7},
#                          {"PeriodStart": 20161, "PeriodEnd": 30240,
#                              "MinHeight": 0.5, "MaxHeight": 0.8},
#                          {"PeriodStart": 30241, "PeriodEnd": 40320,
#                              "MinHeight": 0.6, "MaxHeight": 0.8},
#                          {"PeriodStart": 40321, "PeriodEnd": 50400,
#                              "MinHeight": 0.7, "MaxHeight": 1},
#                          {"PeriodStart": 50401, "PeriodEnd": 60400,
#                              "MinHeight": 1, "MaxHeight": 2},
#                          {"PeriodStart": 60481, "PeriodEnd": 70560,
#                              "MinHeight": 1, "MaxHeight": 2.5},
#                          {"PeriodStart": 70561, "PeriodEnd": 80640,
#                              "MinHeight": 2, "MaxHeight": 3.5},
#                          {"PeriodStart": 80641, "PeriodEnd": 90720,
#                              "MinHeight": 2, "MaxHeight": 4},
#                          {"PeriodStart": 90721, "PeriodEnd": 100800,
#                              "MinHeight": 4, "MaxHeight": 5.5},
#                          {"PeriodStart": 110881, "PeriodEnd": 120960,
#                              "MinHeight": 5, "MaxHeight": 6},
#                          {"PeriodStart": 120961, "PeriodEnd": 131040,
#                              "MinHeight": 5, "MaxHeight": 6},
#                          {"PeriodStart": 141121, "PeriodEnd": 151200,
#                              "MinHeight": 6, "MaxHeight": 7},
#                          {"PeriodStart": 151201, "PeriodEnd": 161280,
#                              "MinHeight": 6, "MaxHeight": 7},
#                          {"PeriodStart": 161281, "PeriodEnd": 171360,
#                              "MinHeight": 6, "MaxHeight": 7},
#                          {"PeriodStart": 171361, "PeriodEnd": 181400,
#                           "MinHeight": 6.5, "MaxHeight": 8},
#                          {"PeriodStart": 181440, "PeriodEnd": 191520,
#                              "MinHeight": 1, "MaxHeight": 4},
#                          {"PeriodStart": 191521, "PeriodEnd": 201600,
#                           "MinHeight": 1, "MaxHeight": 3.5},
#                          {"PeriodStart": 131041, "PeriodEnd": 141120,
#                              "MinHeight": 5, "MaxHeight": 7},
#                          {"PeriodStart": 201601, "PeriodEnd": 211680,
#                              "MinHeight": 2, "MaxHeight": 4},
#                          {"PeriodStart": 211681, "PeriodEnd": 221760,
#                              "MinHeight": 1, "MaxHeight": 4},
#                          {"PeriodStart": 221761, "PeriodEnd": 10000000,
#                              "MinHeight": 1, "MaxHeight": 4}])
# # print(res.inserted_ids)


# # rice database entry

# res = rice.insert_many([{"PeriodStart": 0, "PeriodEnd": 10080,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 10081, "PeriodEnd": 20161,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 20161, "PeriodEnd": 30240,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 30241, "PeriodEnd": 40320,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 40321, "PeriodEnd": 50400,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 50401, "PeriodEnd": 60400,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 60481, "PeriodEnd": 70560,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 70561, "PeriodEnd": 80640,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 80641, "PeriodEnd": 90720,
#                             "MinHeight": 5, "MaxHeight": 6},
#                         {"PeriodStart": 90721, "PeriodEnd": 100800,
#                             "MinHeight": 5, "MaxHeight": 6},
#                         {"PeriodStart": 110881, "PeriodEnd": 120960,
#                             "MinHeight": 6, "MaxHeight": 6},
#                         {"PeriodStart": 120961, "PeriodEnd": 131040,
#                             "MinHeight": 6, "MaxHeight": 7},
#                         {"PeriodStart": 131041, "PeriodEnd": 141120,
#                             "MinHeight": 6, "MaxHeight": 7},
#                         {"PeriodStart": 141121, "PeriodEnd": 151200,
#                             "MinHeight": 6, "MaxHeight": 6},
#                         {"PeriodStart": 151201, "PeriodEnd": 161280,
#                             "MinHeight": 6, "MaxHeight": 6},
#                         {"PeriodStart": 161281, "PeriodEnd": 171360,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 171361, "PeriodEnd": 181400,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 181440, "PeriodEnd": 191520,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 191521, "PeriodEnd": 201600,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 201601, "PeriodEnd": 211680,
#                             "MinHeight": 4, "MaxHeight": 5},
#                         {"PeriodStart": 211681, "PeriodEnd": 221760,
#                             "MinHeight": 5, "MaxHeight": 5},
#                         {"PeriodStart": 221761, "PeriodEnd": 10000000, 
#                             "MinHeight": 5, "MaxHeight": 5}])


# # grass database entry

# res = grass.insert_many([{"PeriodStart": 0, "PeriodEnd": 10080,
#                              "MinHeight": 0.5, "MaxHeight": 0.7},
#                          {"PeriodStart": 10081, "PeriodEnd": 20161,
#                              "MinHeight": 0.5, "MaxHeight": 0.7},
#                          {"PeriodStart": 20161, "PeriodEnd": 30240,
#                              "MinHeight": 0.5, "MaxHeight": 0.8},
#                          {"PeriodStart": 30241, "PeriodEnd": 40320,
#                              "MinHeight": 0.6, "MaxHeight": 0.7},
#                          {"PeriodStart": 40321, "PeriodEnd": 50400,
#                              "MinHeight": 0.8, "MaxHeight": 1},
#                          {"PeriodStart": 50401, "PeriodEnd": 60400,
#                              "MinHeight": 0.8, "MaxHeight": 1},
#                          {"PeriodStart": 60481, "PeriodEnd": 70560,
#                              "MinHeight": 0.8, "MaxHeight": 1},
#                          {"PeriodStart": 70561, "PeriodEnd": 80640,
#                              "MinHeight": 0.8, "MaxHeight": 1},
#                          {"PeriodStart": 80641, "PeriodEnd": 90720,
#                              "MinHeight": 1, "MaxHeight": 1.2},
#                          {"PeriodStart": 90721, "PeriodEnd": 100800,
#                              "MinHeight": 1, "MaxHeight": 1.2},
#                          {"PeriodStart": 110881, "PeriodEnd": 120960,
#                              "MinHeight": 1, "MaxHeight": 1.2},
#                          {"PeriodStart": 120961, "PeriodEnd": 131040,
#                           "MinHeight": 1, "MaxHeight": 1.4},
#                          {"PeriodStart": 131041, "PeriodEnd": 141120,
#                           "MinHeight": 1.2, "MaxHeight": 1.4},
#                          {"PeriodStart": 141121, "PeriodEnd": 151200,
#                           "MinHeight": 1.2, "MaxHeight": 1.6},
#                          {"PeriodStart": 151201, "PeriodEnd": 161280,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 161281, "PeriodEnd": 171360,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 171361, "PeriodEnd": 181400,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 181440, "PeriodEnd": 191520,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 191521, "PeriodEnd": 201600,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 201601, "PeriodEnd": 211680,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 211681, "PeriodEnd": 221760,
#                           "MinHeight": 2, "MaxHeight": 2.5},
#                          {"PeriodStart": 221761, "PeriodEnd": 10000000,
#                           "MinHeight": 2.5, "MaxHeight": 3}
#                          ])



#print(records.count_documents({}))           # count the number of documents in the collection

# x=list(records.find())                      #print the collection
# for i in x:
#     print(i)

