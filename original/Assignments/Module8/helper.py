y_test = [2, 2, 4, 4, 2, 2, 2, 4, 2, 2, 4, 2, 4, 2, 2, 2, 4, 4, 4, 2, 2, 2, 4,
       2, 4, 4, 2, 2, 2, 4, 2, 4, 4, 2, 2, 2, 4, 4, 2, 4, 2, 2, 2, 2, 2, 2,
       2, 4, 2, 2, 4, 2, 4, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4,
       4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 4, 2, 4, 2, 2, 4, 2, 2, 4, 2, 4, 2,
       4, 4, 4, 2, 4, 4, 4, 2, 2, 2, 4, 4, 2, 2, 4, 4, 2, 2, 4, 2, 2, 4, 2,
       2, 2, 4, 2, 2, 2, 4, 2, 2, 4, 4, 2, 4, 2, 4, 2, 2, 4, 2, 2, 4, 2]

y_train = [4, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2, 4, 4, 2, 2, 2, 2, 4, 4, 2, 4,
       4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 4, 2, 2, 4, 4, 2,
       4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 4,
       2, 4, 2, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 2, 2, 4, 4, 2, 4, 2,
       4, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2,
       2, 2, 2, 2, 4, 2, 2, 4, 2, 4, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4,
       2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 4,
       4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 4, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2,
       2, 4, 4, 4, 4, 2, 4, 2, 4, 2, 4, 4, 4, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2,
       2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       4, 2, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 4, 2, 4, 2, 4, 2, 2, 2,
       2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2,
       2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 4, 4,
       2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2, 4, 2, 4, 2, 2, 2, 4, 4,
       4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2,
       2, 4, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 4, 2, 4, 4, 2, 2, 2, 2, 2, 2,
       2, 4, 2, 2, 2, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 2, 4, 2, 4, 2, 2,
       4, 2, 4, 4, 4, 2, 2, 2, 4, 2, 4, 4, 4, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2,
       4, 4, 2, 2, 2, 4, 4, 2, 2, 4, 2, 2, 2, 4, 4, 2, 2, 2, 4, 2, 2, 2, 4,
       2, 4, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 2, 2, 4, 4, 4, 2, 2, 4,
       2, 2, 2, 2, 2, 4, 2, 4, 4, 2, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2, 4,
       2, 2, 4, 2, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 2, 4,
       4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 2,
       2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 4]

X_train = [[752904, 10, 1, 1, 1, 2, 10, 5, 4, 1],
 [1218860, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [411453, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1237674, 3, 1, 2, 1, 2, 1, 2, 1, 1],
 [1168359, 8, 2, 3, 1, 6, 3, 7, 1, 1],
 [385103, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1201834, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [1201870, 4, 1, 1, 3, 1, 1, 2, 1, 1],
 [242970, 5, 7, 7, 1, 5, 8, 3, 4, 1],
 [1242364, 8, 10, 10, 8, 6, 9, 3, 10, 10],
 [1272039, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [543558, 6, 1, 3, 1, 4, 5, 5, 10, 1],
 [1287971, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [695091, 5, 10, 10, 5, 4, 5, 4, 4, 1],
 [859164, 5, 3, 3, 1, 3, 3, 3, 3, 3],
 [535331, 3, 1, 1, 1, 3, 1, 2, 1, 1],
 [1079304, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1181567, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1182404, 4, 2, 1, 1, 2, 1, 1, 1, 1],
 [1211265, 3, 10, 8, 7, 6, 9, 9, 3, 8],
 [1196915, 10, 7, 7, 4, 5, 10, 5, 7, 2],
 [333093, 1, 1, 1, 1, 3, 1, 1, 1, 1],
 [888820, 5, 10, 10, 3, 7, 3, 8, 10, 2],
 [1352848, 3, 10, 7, 8, 5, 8, 7, 4, 1],
 [601265, 10, 4, 4, 6, 2, 10, 2, 3, 1],
 [474162, 8, 7, 8, 5, 5, 10, 9, 10, 1],
 [1041801, 5, 3, 3, 3, 2, 3, 4, 4, 1],
 [1198128, 10, 8, 10, 10, 6, 1, 3, 1, 10],
 [1365075, 4, 1, 4, 1, 2, 1, 1, 1, 1],
 [1266124, 5, 1, 2, 1, 2, 1, 1, 1, 1],
 [1197979, 4, 1, 1, 1, 2, 2, 3, 2, 1],
 [764974, 5, 1, 1, 1, 2, 1, 3, 1, 2],
 [1137156, 2, 2, 2, 1, 1, 1, 7, 1, 1],
 [1160476, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [142932, 7, 6, 10, 5, 3, 10, 9, 10, 2],
 [1120559, 8, 3, 8, 3, 4, 9, 8, 9, 8],
 [1254538, 8, 10, 10, 10, 6, 10, 10, 10, 1],
 [688033, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [428598, 1, 1, 3, 1, 1, 1, 2, 1, 1],
 [1294413, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1168736, 5, 6, 6, 2, 4, 10, 3, 6, 1],
 [1288608, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1186936, 2, 1, 3, 2, 2, 1, 2, 1, 1],
 [1190386, 4, 6, 6, 5, 7, 6, 7, 7, 3],
 [1047630, 7, 4, 6, 4, 6, 1, 4, 3, 1],
 [1270479, 5, 1, 3, 3, 2, 2, 2, 3, 1],
 [1225799, 10, 6, 4, 3, 10, 10, 9, 10, 1],
 [1018099, 1, 1, 1, 1, 2, 10, 3, 1, 1],
 [452264, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1125035, 9, 4, 5, 10, 6, 10, 4, 8, 1],
 [822829, 8, 10, 10, 10, 6, 10, 10, 10, 10],
 [666090, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [640712, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1348851, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1260659, 3, 1, 4, 1, 2, 1, 1, 1, 1],
 [1212422, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1239420, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [431495, 3, 1, 1, 1, 2, 1, 3, 2, 1],
 [342245, 1, 1, 3, 1, 2, 1, 1, 1, 1],
 [1157734, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [353098, 4, 1, 1, 2, 2, 1, 1, 1, 1],
 [897471, 4, 8, 8, 5, 4, 5, 10, 4, 1],
 [1174057, 1, 1, 2, 2, 2, 1, 3, 1, 1],
 [1113061, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1345452, 1, 1, 3, 1, 2, 1, 2, 1, 1],
 [1320304, 3, 1, 2, 2, 2, 1, 1, 1, 1],
 [1304595, 3, 1, 1, 1, 1, 1, 2, 1, 1],
 [659642, 10, 8, 4, 4, 4, 10, 3, 10, 4],
 [1171845, 8, 6, 4, 3, 5, 9, 3, 1, 1],
 [1133991, 4, 1, 1, 1, 1, 1, 2, 1, 1],
 [1219859, 8, 10, 8, 8, 4, 8, 7, 7, 1],
 [770066, 5, 2, 2, 2, 2, 1, 2, 2, 1],
 [1213375, 8, 4, 4, 5, 4, 7, 7, 8, 2],
 [721482, 4, 4, 4, 4, 6, 5, 7, 3, 1],
 [1257200, 10, 10, 10, 7, 10, 10, 8, 2, 1],
 [560680, 3, 1, 2, 1, 2, 1, 2, 1, 1],
 [805448, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1228311, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [1297522, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1306282, 6, 6, 7, 10, 3, 10, 8, 10, 2],
 [1214966, 9, 7, 7, 5, 5, 10, 7, 8, 3],
 [1323477, 1, 2, 1, 3, 2, 1, 2, 1, 1],
 [677910, 5, 2, 2, 4, 2, 4, 1, 1, 1],
 [1318169, 9, 10, 10, 10, 10, 5, 10, 10, 10],
 [1238633, 10, 10, 10, 6, 8, 4, 8, 5, 1],
 [897172, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1180831, 3, 1, 1, 1, 3, 1, 2, 1, 1],
 [1202812, 5, 3, 3, 3, 6, 10, 3, 1, 1],
 [1205579, 8, 7, 6, 4, 4, 10, 5, 1, 1],
 [1311108, 1, 1, 1, 3, 2, 1, 1, 1, 1],
 [866325, 8, 10, 5, 3, 8, 4, 4, 10, 3],
 [1202125, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1166630, 7, 5, 6, 10, 5, 10, 7, 9, 4],
 [608157, 10, 4, 3, 10, 4, 10, 10, 1, 1],
 [1368882, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1056171, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1220330, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1268275, 9, 8, 8, 9, 6, 3, 4, 1, 1],
 [1334071, 4, 1, 1, 1, 2, 3, 2, 1, 1],
 [1165926, 9, 6, 9, 2, 10, 6, 2, 9, 10],
 [1223543, 1, 2, 1, 3, 2, 1, 1, 2, 1],
 [188336, 5, 3, 2, 8, 5, 10, 8, 1, 2],
 [763235, 3, 1, 1, 1, 2, 1, 2, 1, 2],
 [636437, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1156948, 3, 1, 1, 2, 2, 1, 1, 1, 1],
 [831268, 1, 1, 1, 1, 1, 1, 1, 3, 1],
 [1206089, 2, 1, 1, 1, 1, 1, 3, 1, 1],
 [1170419, 10, 10, 10, 8, 2, 10, 4, 1, 1],
 [1000025, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1106095, 4, 1, 1, 3, 2, 1, 3, 1, 1],
 [1201936, 5, 10, 10, 3, 8, 1, 5, 10, 3],
 [826923, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1070522, 3, 1, 1, 1, 1, 1, 2, 1, 1],
 [1241559, 10, 8, 8, 2, 8, 10, 4, 8, 10],
 [1328331, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [493452, 4, 1, 2, 1, 2, 1, 2, 1, 1],
 [1223426, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [486662, 2, 1, 1, 2, 2, 1, 3, 1, 1],
 [1224565, 6, 1, 1, 1, 2, 1, 3, 1, 1],
 [1171710, 6, 5, 4, 4, 3, 9, 7, 8, 3],
 [1155967, 5, 1, 2, 10, 4, 5, 2, 1, 1],
 [1296263, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1230175, 10, 10, 10, 3, 10, 10, 9, 10, 1],
 [1202253, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1168736, 10, 10, 10, 10, 10, 1, 8, 8, 8],
 [1171795, 1, 3, 1, 2, 2, 2, 5, 3, 2],
 [1223967, 6, 1, 3, 1, 2, 1, 3, 1, 1],
 [1239347, 8, 7, 8, 5, 10, 10, 7, 2, 1],
 [1222464, 6, 10, 10, 10, 4, 10, 7, 10, 1],
 [1116116, 9, 10, 10, 1, 10, 8, 3, 3, 1],
 [1229929, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1276091, 1, 3, 1, 1, 2, 1, 2, 2, 1],
 [1177027, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1206314, 1, 2, 3, 1, 2, 1, 1, 1, 1],
 [654546, 1, 1, 1, 3, 2, 1, 1, 1, 1],
 [837082, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [803531, 5, 10, 10, 10, 5, 2, 8, 5, 1],
 [1230688, 7, 4, 7, 4, 3, 7, 7, 6, 1],
 [1066979, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1269574, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1293966, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1016277, 6, 8, 8, 1, 3, 4, 3, 7, 1],
 [1182404, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1212232, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1253505, 2, 3, 1, 1, 5, 1, 1, 1, 1],
 [352431, 10, 5, 10, 3, 5, 8, 7, 8, 3],
 [1321264, 5, 2, 2, 2, 1, 1, 2, 1, 1],
 [1257366, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1231387, 6, 8, 7, 5, 6, 8, 8, 9, 2],
 [1344449, 1, 1, 1, 1, 1, 1, 2, 1, 1],
 [896404, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [1182404, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1058849, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1297327, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1257938, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [527337, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1315807, 5, 10, 10, 10, 10, 2, 10, 10, 10],
 [867392, 4, 2, 2, 1, 2, 1, 2, 1, 1],
 [1173235, 3, 3, 2, 1, 2, 3, 3, 1, 1],
 [1238777, 6, 1, 1, 3, 2, 1, 1, 1, 1],
 [1054590, 7, 3, 2, 10, 5, 10, 5, 4, 4],
 [1118039, 5, 3, 4, 1, 8, 10, 4, 9, 1],
 [684955, 2, 1, 1, 1, 3, 1, 2, 1, 1],
 [1177399, 8, 3, 5, 4, 5, 10, 1, 6, 2],
 [1298360, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1347749, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1287282, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1294261, 4, 10, 8, 5, 4, 1, 10, 1, 1],
 [1183516, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1336798, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1018561, 2, 1, 2, 1, 2, 1, 3, 1, 1],
 [897471, 4, 8, 6, 4, 3, 4, 10, 6, 1],
 [733823, 5, 4, 6, 10, 2, 10, 4, 1, 1],
 [1183596, 3, 1, 3, 1, 3, 4, 1, 1, 1],
 [1211202, 7, 5, 10, 10, 10, 10, 4, 10, 3],
 [411453, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1193210, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [1112209, 8, 10, 10, 1, 3, 6, 3, 9, 1],
 [1071760, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [1213273, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1167471, 4, 1, 2, 1, 2, 1, 3, 1, 1],
 [1299924, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1277792, 5, 1, 1, 3, 2, 1, 1, 1, 1],
 [1347943, 5, 2, 2, 2, 2, 1, 1, 1, 2],
 [1285531, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1113483, 5, 2, 3, 1, 6, 10, 5, 1, 1],
 [1116116, 9, 10, 10, 1, 10, 8, 3, 3, 1],
 [1266154, 8, 7, 8, 2, 4, 2, 5, 10, 1],
 [390840, 8, 4, 7, 1, 3, 10, 3, 9, 2],
 [1238410, 2, 3, 1, 1, 3, 1, 1, 1, 1],
 [320675, 3, 3, 5, 2, 3, 10, 7, 1, 1],
 [1116715, 5, 1, 1, 1, 3, 2, 2, 2, 1],
 [1222047, 10, 10, 10, 10, 3, 10, 10, 6, 1],
 [1223306, 3, 1, 1, 1, 2, 4, 1, 1, 1],
 [846423, 10, 6, 3, 6, 4, 10, 7, 8, 4],
 [1200847, 6, 10, 10, 10, 8, 10, 10, 10, 7],
 [1091262, 2, 5, 3, 3, 6, 7, 7, 5, 1],
 [654244, 1, 1, 1, 1, 1, 1, 2, 1, 1],
 [690557, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [691628, 8, 6, 4, 10, 10, 1, 3, 5, 1],
 [1276091, 5, 1, 1, 3, 4, 1, 3, 2, 1],
 [1320077, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1333495, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1199219, 1, 1, 1, 2, 1, 1, 1, 1, 1],
 [1176881, 7, 5, 3, 7, 4, 10, 7, 5, 5],
 [1196295, 9, 9, 10, 3, 6, 10, 7, 10, 6],
 [836433, 5, 1, 1, 3, 2, 1, 1, 1, 1],
 [1115293, 1, 1, 1, 1, 2, 2, 2, 1, 1],
 [1277629, 5, 1, 1, 1, 2, 1, 2, 2, 1],
 [709287, 6, 8, 7, 8, 6, 8, 8, 9, 1],
 [1334667, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1306339, 4, 4, 2, 1, 2, 5, 2, 1, 2],
 [859350, 8, 10, 10, 7, 10, 10, 7, 3, 8],
 [492561, 4, 3, 2, 1, 3, 1, 2, 1, 1],
 [743348, 3, 2, 2, 1, 2, 1, 2, 3, 1],
 [1325159, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1197440, 1, 1, 1, 2, 1, 3, 1, 1, 7],
 [1110503, 5, 5, 5, 8, 10, 8, 7, 3, 7],
 [1076352, 3, 6, 4, 10, 3, 3, 3, 4, 1],
 [566509, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1114570, 2, 1, 1, 1, 2, 1, 2, 2, 1],
 [1239232, 3, 3, 2, 6, 3, 3, 3, 5, 1],
 [1227244, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [733639, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1132347, 1, 1, 4, 1, 2, 1, 2, 1, 1],
 [561477, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1299596, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1017023, 4, 1, 1, 3, 2, 1, 3, 1, 1],
 [534555, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1197527, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1238948, 8, 5, 6, 2, 3, 10, 6, 6, 1],
 [1115293, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1017122, 8, 10, 10, 8, 7, 10, 9, 7, 1],
 [1184241, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1253917, 4, 1, 1, 2, 2, 1, 2, 1, 1],
 [1182410, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [824249, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1235807, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1056784, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1268952, 10, 10, 7, 8, 7, 1, 10, 10, 3],
 [527363, 8, 10, 10, 10, 8, 10, 10, 7, 3],
 [606722, 5, 5, 7, 8, 6, 10, 7, 4, 1],
 [476903, 10, 5, 7, 3, 3, 7, 3, 3, 8],
 [1354840, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [560680, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1227481, 10, 5, 7, 4, 4, 10, 8, 9, 1],
 [1275807, 4, 2, 4, 3, 2, 2, 2, 1, 1],
 [785615, 8, 6, 7, 3, 3, 10, 3, 4, 2],
 [1257608, 6, 1, 1, 1, 1, 1, 1, 1, 1],
 [1174131, 10, 10, 10, 2, 10, 10, 5, 3, 3],
 [1147044, 3, 1, 1, 1, 2, 2, 7, 1, 1],
 [566346, 3, 1, 1, 1, 2, 1, 2, 3, 1],
 [1043999, 1, 1, 1, 1, 2, 3, 3, 1, 1],
 [1295508, 1, 1, 1, 1, 2, 4, 1, 1, 1],
 [1369821, 10, 10, 10, 10, 5, 10, 10, 10, 7],
 [1355260, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1197993, 5, 6, 7, 8, 8, 10, 3, 10, 3],
 [466906, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1287775, 5, 1, 1, 2, 2, 2, 3, 1, 1],
 [1158247, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1293439, 6, 9, 7, 5, 5, 8, 4, 2, 1],
 [1084139, 6, 3, 2, 1, 3, 4, 4, 1, 1],
 [1302428, 5, 3, 2, 4, 2, 1, 1, 1, 1],
 [1016634, 2, 3, 1, 1, 2, 1, 2, 1, 1],
 [1216694, 10, 8, 8, 4, 10, 10, 8, 1, 1],
 [1213383, 5, 1, 1, 4, 2, 1, 3, 1, 1],
 [1173514, 1, 1, 1, 1, 4, 3, 1, 1, 1],
 [1135090, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [695219, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1199731, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1171710, 1, 1, 1, 1, 2, 1, 2, 3, 1],
 [1048672, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1116998, 10, 4, 2, 1, 3, 2, 4, 3, 10],
 [1196475, 3, 2, 1, 1, 2, 1, 2, 2, 1],
 [1170420, 1, 6, 8, 10, 8, 10, 5, 7, 1],
 [1296593, 5, 2, 1, 1, 2, 1, 1, 1, 1],
 [13454352, 1, 1, 3, 1, 2, 1, 2, 1, 1],
 [814911, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [873549, 10, 3, 5, 4, 3, 7, 3, 5, 3],
 [1371920, 5, 1, 1, 1, 2, 1, 3, 2, 1],
 [1255384, 3, 2, 2, 3, 2, 3, 3, 1, 1],
 [769612, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1164066, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1320077, 1, 1, 1, 1, 1, 1, 2, 1, 1],
 [1147748, 5, 10, 6, 1, 10, 4, 4, 10, 10],
 [1320141, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [888169, 3, 2, 2, 1, 4, 3, 2, 1, 1],
 [1240603, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1217264, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1187805, 8, 8, 7, 4, 10, 10, 7, 8, 7],
 [1276091, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1190485, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1099510, 10, 4, 3, 1, 3, 3, 6, 5, 2],
 [8233704, 4, 1, 1, 1, 1, 1, 2, 1, 1],
 [536708, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1290203, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1331405, 4, 1, 1, 1, 2, 1, 3, 2, 1],
 [797327, 6, 5, 5, 8, 4, 10, 3, 4, 1],
 [263538, 5, 10, 10, 6, 10, 10, 10, 6, 5],
 [1225382, 6, 2, 3, 1, 2, 1, 1, 1, 1],
 [1217952, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [603148, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [493452, 1, 1, 3, 1, 2, 1, 1, 1, 1],
 [1123061, 6, 10, 2, 8, 10, 2, 7, 8, 10],
 [1015425, 3, 1, 1, 1, 2, 2, 3, 1, 1],
 [855524, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1228152, 8, 9, 9, 5, 3, 5, 7, 7, 1],
 [1330361, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1188472, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [636130, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [167528, 4, 1, 1, 1, 2, 1, 3, 6, 1],
 [672113, 7, 5, 6, 10, 4, 10, 5, 3, 1],
 [878358, 5, 7, 10, 6, 5, 10, 7, 5, 1],
 [1173347, 8, 3, 3, 1, 2, 2, 3, 2, 1],
 [1334015, 7, 8, 8, 7, 3, 10, 7, 2, 3],
 [841769, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1343068, 8, 4, 4, 1, 6, 10, 2, 5, 2],
 [1321942, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1204898, 6, 1, 1, 1, 2, 1, 3, 1, 1],
 [1083817, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1080233, 7, 6, 6, 3, 2, 10, 7, 1, 1],
 [1200892, 8, 6, 5, 4, 3, 10, 6, 1, 1],
 [877943, 3, 10, 3, 10, 6, 10, 5, 1, 4],
 [1131411, 1, 1, 1, 2, 2, 1, 2, 1, 1],
 [1061990, 1, 1, 3, 2, 2, 1, 3, 1, 1],
 [1042252, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1350568, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1171578, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1212422, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1183240, 4, 1, 2, 1, 2, 1, 2, 1, 1],
 [1268804, 3, 1, 1, 1, 2, 5, 1, 1, 1],
 [1298484, 10, 3, 4, 5, 3, 10, 4, 1, 1],
 [274137, 8, 8, 9, 4, 5, 10, 7, 8, 1],
 [749653, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1176187, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1149548, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1204558, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1345593, 3, 1, 1, 3, 2, 1, 2, 1, 1],
 [1096352, 6, 3, 3, 3, 3, 2, 6, 1, 1],
 [1333063, 5, 1, 3, 1, 2, 1, 3, 1, 1],
 [303213, 10, 4, 4, 10, 6, 10, 5, 5, 1],
 [1243256, 10, 4, 3, 2, 3, 10, 5, 3, 2],
 [1181356, 5, 1, 1, 1, 2, 2, 3, 3, 1],
 [1075123, 3, 1, 2, 1, 2, 1, 2, 1, 1],
 [1156272, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1293439, 3, 2, 2, 3, 2, 1, 1, 1, 1],
 [640744, 10, 10, 10, 7, 9, 10, 7, 10, 10],
 [1105257, 3, 7, 7, 4, 4, 9, 4, 8, 1],
 [160296, 5, 8, 8, 10, 5, 10, 8, 10, 3],
 [857774, 4, 1, 1, 1, 3, 1, 2, 2, 1],
 [1116132, 6, 3, 4, 1, 5, 2, 3, 9, 1],
 [1354840, 5, 3, 2, 1, 3, 1, 1, 1, 1],
 [1218105, 5, 10, 10, 9, 6, 10, 7, 10, 5],
 [780555, 5, 1, 1, 6, 3, 1, 2, 1, 1],
 [1067444, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1236837, 2, 3, 2, 2, 2, 2, 3, 1, 1],
 [1353092, 3, 2, 1, 2, 2, 1, 3, 1, 1],
 [1289391, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [320675, 3, 3, 5, 2, 3, 10, 7, 1, 1],
 [657753, 3, 1, 1, 4, 3, 1, 2, 2, 1],
 [1193544, 5, 7, 9, 8, 6, 10, 8, 10, 1],
 [1227210, 10, 5, 5, 6, 3, 10, 7, 9, 2],
 [704097, 1, 1, 1, 1, 1, 1, 2, 1, 1],
 [1073836, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1257648, 4, 3, 3, 1, 2, 1, 3, 3, 1],
 [673637, 3, 1, 1, 1, 2, 5, 5, 1, 1],
 [1131294, 1, 1, 2, 1, 2, 2, 4, 2, 1],
 [1234554, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [666942, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1080185, 10, 10, 10, 8, 6, 1, 8, 9, 1],
 [1116192, 5, 1, 2, 1, 2, 1, 3, 1, 1],
 [1070935, 3, 1, 1, 1, 1, 1, 2, 1, 1],
 [1227081, 3, 1, 1, 3, 2, 1, 1, 1, 1],
 [1352663, 5, 4, 6, 8, 4, 1, 8, 10, 1],
 [1261751, 5, 1, 1, 1, 2, 1, 2, 2, 1],
 [1311875, 5, 1, 2, 1, 2, 1, 1, 1, 1],
 [1226612, 7, 5, 6, 3, 3, 8, 7, 4, 1],
 [1107684, 6, 10, 5, 5, 4, 10, 6, 10, 1],
 [1295186, 10, 10, 10, 1, 6, 1, 2, 8, 1],
 [1183911, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1223793, 6, 10, 7, 7, 6, 4, 8, 10, 2],
 [1315506, 4, 8, 6, 3, 4, 10, 7, 1, 1],
 [1295529, 2, 5, 7, 6, 4, 10, 7, 6, 1],
 [1311033, 1, 2, 2, 1, 2, 1, 1, 1, 1],
 [1276091, 3, 1, 1, 3, 1, 1, 3, 1, 1],
 [1121732, 1, 1, 1, 1, 2, 1, 3, 2, 1],
 [1065726, 5, 2, 3, 4, 2, 7, 3, 6, 1],
 [1168278, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1226012, 4, 1, 1, 3, 1, 5, 2, 1, 1],
 [1179818, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [888523, 4, 4, 4, 2, 2, 3, 2, 1, 1],
 [1173216, 10, 10, 10, 3, 10, 8, 8, 1, 1],
 [1200772, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1221863, 10, 10, 10, 10, 7, 10, 7, 10, 4],
 [1230994, 4, 5, 5, 8, 6, 10, 10, 7, 1],
 [492268, 10, 4, 6, 1, 2, 10, 5, 3, 1],
 [1334659, 5, 2, 4, 1, 1, 1, 1, 1, 1],
 [1328755, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1158157, 5, 1, 1, 1, 2, 2, 2, 1, 1],
 [63375, 9, 1, 2, 6, 4, 10, 7, 7, 2],
 [787451, 5, 1, 2, 1, 2, 1, 1, 1, 1],
 [809912, 10, 3, 3, 1, 2, 10, 7, 6, 1],
 [1174428, 5, 3, 5, 1, 8, 10, 5, 3, 1],
 [412300, 10, 4, 5, 4, 3, 5, 7, 3, 1],
 [1236043, 3, 3, 2, 1, 3, 1, 3, 6, 1],
 [1268313, 5, 1, 1, 3, 2, 1, 1, 1, 1],
 [1173681, 3, 2, 1, 1, 2, 2, 3, 1, 1],
 [1299161, 4, 8, 7, 10, 4, 10, 7, 5, 1],
 [1066373, 3, 2, 1, 1, 1, 1, 2, 1, 1],
 [1172152, 10, 3, 3, 10, 2, 10, 7, 3, 3],
 [1190394, 4, 1, 1, 1, 2, 3, 1, 1, 1],
 [1193091, 1, 2, 2, 1, 2, 1, 2, 1, 1],
 [1184586, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1296025, 4, 1, 2, 1, 2, 1, 1, 1, 1],
 [1183983, 9, 5, 5, 4, 4, 5, 4, 3, 3],
 [324427, 10, 8, 8, 2, 3, 4, 8, 7, 8],
 [798429, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1324681, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [1182404, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1296572, 10, 9, 8, 7, 6, 4, 7, 10, 3],
 [1258549, 9, 10, 10, 10, 10, 10, 10, 10, 1],
 [1050718, 6, 1, 1, 1, 2, 1, 3, 1, 1],
 [814265, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [667204, 7, 8, 7, 6, 4, 3, 8, 8, 4],
 [456282, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1231706, 8, 4, 6, 3, 3, 1, 4, 3, 1],
 [1165297, 2, 1, 1, 2, 2, 1, 1, 1, 1],
 [837480, 7, 4, 4, 3, 4, 10, 6, 9, 1],
 [555977, 5, 6, 6, 8, 6, 10, 4, 10, 4],
 [625201, 8, 2, 1, 1, 5, 1, 1, 1, 1],
 [1333877, 5, 4, 5, 1, 8, 1, 3, 6, 1],
 [1267898, 5, 1, 3, 1, 2, 1, 1, 1, 1],
 [1210963, 10, 10, 10, 8, 6, 8, 7, 10, 1],
 [1071084, 3, 3, 2, 2, 3, 1, 1, 2, 3],
 [1061990, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [466906, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [508234, 7, 4, 5, 10, 2, 10, 3, 8, 2],
 [1339781, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1207986, 5, 8, 4, 10, 5, 8, 9, 10, 1],
 [1074610, 2, 1, 1, 2, 2, 1, 3, 1, 1],
 [1143978, 5, 2, 1, 1, 2, 1, 3, 1, 1],
 [730881, 7, 6, 3, 2, 5, 10, 7, 4, 6],
 [1036172, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1103722, 1, 1, 1, 1, 2, 1, 2, 1, 2],
 [1152331, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1081791, 6, 2, 1, 1, 1, 1, 7, 1, 1],
 [1115282, 5, 3, 5, 5, 3, 3, 4, 10, 1],
 [1102573, 5, 6, 5, 6, 10, 1, 3, 1, 1],
 [1258556, 5, 3, 6, 1, 2, 1, 1, 1, 1],
 [695091, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1222936, 8, 7, 8, 7, 5, 5, 5, 10, 2],
 [1189286, 10, 10, 8, 6, 4, 5, 8, 10, 1],
 [1176406, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1272166, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1166654, 10, 3, 5, 1, 10, 5, 3, 10, 2],
 [1151734, 10, 8, 7, 4, 3, 10, 7, 9, 1],
 [1180194, 5, 10, 8, 10, 8, 10, 3, 6, 3],
 [1059552, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [714039, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1344121, 8, 10, 4, 4, 8, 10, 8, 2, 1],
 [1026122, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [798429, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1196263, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1218860, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [1002504, 3, 2, 2, 2, 2, 1, 3, 2, 1],
 [1343374, 10, 10, 8, 10, 6, 5, 10, 3, 1],
 [1213784, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [653777, 8, 3, 4, 9, 3, 10, 3, 3, 1],
 [314428, 7, 9, 4, 10, 10, 3, 5, 3, 3],
 [1140597, 7, 1, 2, 3, 2, 1, 2, 1, 1],
 [1217051, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1165790, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1368267, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1200952, 5, 8, 7, 7, 10, 10, 5, 7, 1],
 [1325309, 4, 1, 2, 1, 2, 1, 2, 1, 1],
 [718641, 1, 1, 1, 1, 5, 1, 3, 1, 1],
 [385103, 5, 1, 2, 1, 2, 1, 3, 1, 1],
 [1114570, 5, 3, 3, 2, 3, 1, 3, 1, 1],
 [1232225, 10, 4, 5, 5, 5, 10, 4, 1, 1],
 [1185610, 1, 1, 1, 1, 3, 2, 2, 1, 1],
 [1206695, 1, 5, 8, 6, 5, 8, 7, 10, 1],
 [1180523, 3, 1, 1, 1, 2, 1, 2, 2, 1],
 [1106829, 7, 8, 7, 2, 4, 8, 3, 8, 2],
 [704097, 1, 1, 1, 1, 1, 1, 2, 1, 1],
 [1219406, 5, 1, 1, 1, 1, 1, 3, 1, 1],
 [1148278, 3, 3, 6, 4, 5, 8, 4, 4, 1],
 [871549, 5, 1, 2, 1, 2, 1, 2, 1, 1],
 [1190546, 2, 1, 1, 1, 2, 5, 1, 1, 1],
 [1238915, 5, 1, 2, 1, 2, 1, 3, 1, 1],
 [1158247, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1147699, 3, 5, 7, 8, 8, 9, 7, 10, 7],
 [827627, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1174057, 4, 2, 1, 1, 2, 2, 3, 1, 1],
 [646904, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1113906, 9, 5, 5, 2, 2, 2, 5, 1, 1],
 [792744, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1182404, 5, 1, 4, 1, 2, 1, 3, 2, 1],
 [1350319, 5, 7, 4, 1, 6, 1, 7, 10, 3],
 [1259008, 8, 8, 9, 6, 6, 3, 10, 10, 1],
 [1103608, 10, 10, 10, 4, 8, 1, 8, 10, 1],
 [1253955, 8, 7, 4, 4, 5, 3, 5, 10, 1],
 [1223003, 5, 3, 3, 1, 2, 1, 2, 1, 1],
 [832567, 4, 2, 3, 5, 3, 8, 7, 6, 1],
 [488173, 1, 4, 3, 10, 4, 10, 5, 6, 1],
 [1265899, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1331412, 5, 7, 10, 10, 5, 10, 10, 10, 1],
 [1111249, 10, 6, 6, 3, 4, 5, 3, 6, 1],
 [1339781, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1178580, 5, 1, 3, 1, 2, 1, 2, 1, 1],
 [1070935, 1, 1, 3, 1, 2, 1, 1, 1, 1],
 [1208301, 1, 2, 3, 1, 2, 1, 3, 1, 1],
 [1277145, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [769612, 3, 1, 1, 2, 2, 1, 1, 1, 1],
 [1192325, 5, 5, 5, 6, 3, 10, 3, 1, 1],
 [1017023, 6, 3, 3, 5, 3, 10, 3, 5, 3],
 [1321348, 2, 1, 1, 1, 2, 1, 2, 1, 1],
 [1321931, 5, 1, 1, 1, 2, 1, 2, 1, 1],
 [1326892, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [428903, 7, 2, 4, 1, 3, 4, 3, 3, 1],
 [635844, 8, 4, 10, 5, 4, 4, 7, 10, 1],
 [558538, 4, 1, 3, 3, 2, 1, 1, 1, 1],
 [1189266, 7, 2, 4, 1, 6, 10, 5, 4, 3],
 [1205138, 5, 8, 8, 8, 5, 10, 7, 8, 1],
 [1167439, 2, 3, 4, 4, 2, 5, 2, 5, 1],
 [1280258, 4, 1, 1, 1, 2, 1, 1, 2, 1],
 [1049837, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1173509, 4, 5, 5, 10, 4, 10, 7, 5, 8],
 [1126417, 10, 6, 4, 1, 3, 4, 3, 2, 3],
 [1299924, 3, 2, 2, 2, 2, 1, 4, 2, 1],
 [654546, 1, 1, 1, 1, 2, 1, 1, 1, 8],
 [1203096, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [1155546, 2, 1, 1, 2, 3, 1, 2, 1, 1],
 [1333104, 3, 1, 2, 1, 2, 1, 3, 1, 1],
 [1238186, 4, 1, 1, 1, 2, 1, 2, 1, 1],
 [760001, 8, 10, 3, 2, 6, 4, 3, 10, 1],
 [1238021, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1041043, 4, 1, 3, 1, 2, 1, 2, 1, 1],
 [1073960, 10, 10, 10, 10, 6, 10, 8, 1, 5],
 [1124651, 1, 3, 3, 2, 2, 1, 7, 2, 1],
 [1031608, 2, 1, 1, 1, 1, 1, 2, 1, 1],
 [529329, 10, 10, 10, 10, 10, 10, 4, 10, 10],
 [1033078, 4, 2, 1, 1, 2, 1, 2, 1, 1],
 [521441, 5, 1, 1, 2, 2, 1, 2, 1, 1],
 [1214092, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1303489, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [378275, 10, 9, 7, 3, 4, 2, 7, 7, 1]]

X_test = [[1173347, 1, 1, 1, 1, 2, 5, 1, 1, 1],
 [1156017, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [706426, 5, 5, 5, 2, 5, 10, 4, 3, 1],
 [1330439, 4, 7, 8, 3, 4, 10, 9, 1, 1],
 [693702, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1277268, 3, 3, 1, 1, 2, 1, 1, 1, 1],
 [1133041, 5, 3, 1, 2, 2, 1, 2, 1, 1],
 [1286943, 8, 10, 10, 10, 7, 5, 4, 8, 7],
 [1002025, 1, 1, 1, 3, 1, 3, 1, 1, 1],
 [324382, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1044572, 8, 7, 5, 10, 7, 9, 5, 5, 4],
 [1197080, 4, 1, 1, 1, 2, 1, 3, 2, 1],
 [1206841, 10, 5, 6, 10, 6, 10, 7, 7, 10],
 [1043068, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1217717, 5, 1, 1, 6, 3, 1, 1, 1, 1],
 [1187457, 3, 1, 1, 3, 8, 1, 5, 8, 1],
 [1241679, 9, 8, 8, 5, 6, 2, 4, 10, 4],
 [1100524, 6, 10, 10, 2, 8, 10, 7, 3, 3],
 [822829, 7, 6, 4, 8, 10, 10, 9, 5, 3],
 [1121919, 5, 1, 3, 1, 2, 1, 2, 1, 1],
 [1214556, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1143978, 4, 1, 1, 2, 2, 1, 2, 1, 1],
 [1185609, 3, 4, 5, 2, 6, 8, 4, 1, 1],
 [1313658, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [760239, 10, 4, 6, 4, 5, 10, 7, 1, 1],
 [1299596, 6, 6, 6, 5, 4, 10, 7, 6, 2],
 [1174841, 5, 3, 1, 1, 2, 1, 1, 1, 1],
 [1033078, 2, 1, 1, 1, 2, 1, 1, 1, 5],
 [1299994, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1072179, 10, 7, 7, 3, 8, 5, 7, 4, 3],
 [1238777, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [557583, 5, 10, 10, 10, 10, 10, 10, 1, 1],
 [1219525, 8, 10, 10, 10, 5, 10, 8, 10, 6],
 [1198641, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1218982, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1198641, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1148873, 3, 6, 6, 6, 5, 10, 6, 8, 3],
 [806423, 8, 5, 5, 5, 2, 10, 4, 3, 1],
 [1105524, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1175937, 5, 4, 6, 7, 9, 7, 8, 10, 1],
 [1133136, 3, 1, 1, 1, 2, 3, 3, 1, 1],
 [128059, 1, 1, 1, 1, 2, 5, 5, 1, 1],
 [1158405, 1, 2, 3, 1, 2, 1, 2, 1, 1],
 [1240603, 3, 1, 1, 1, 1, 1, 1, 1, 1],
 [1268766, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [776715, 3, 1, 1, 1, 3, 2, 1, 1, 1],
 [183913, 1, 2, 2, 1, 2, 1, 1, 1, 1],
 [1257470, 10, 6, 5, 8, 5, 10, 8, 6, 1],
 [1321321, 5, 1, 1, 3, 2, 1, 1, 1, 1],
 [636375, 5, 1, 1, 1, 2, 1, 1, 1, 1],
 [1218741, 10, 10, 9, 3, 7, 5, 3, 5, 1],
 [1231853, 4, 2, 2, 1, 2, 1, 2, 1, 1],
 [1110102, 10, 3, 6, 2, 3, 5, 4, 10, 2],
 [1174009, 5, 1, 1, 2, 1, 1, 2, 1, 1],
 [1257815, 5, 1, 3, 1, 2, 1, 2, 1, 1],
 [1319609, 3, 1, 1, 2, 3, 4, 1, 1, 1],
 [191250, 10, 4, 4, 10, 2, 10, 5, 3, 3],
 [1002945, 5, 4, 4, 5, 7, 10, 3, 2, 1],
 [1240337, 5, 2, 2, 2, 2, 2, 3, 2, 2],
 [1294562, 10, 8, 10, 1, 3, 10, 5, 1, 1],
 [1199983, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [734111, 1, 1, 1, 1, 2, 2, 1, 1, 1],
 [1277018, 2, 1, 1, 1, 2, 1, 3, 1, 1],
 [1115762, 3, 1, 1, 1, 2, 1, 1, 1, 1],
 [1197270, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1212251, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [810104, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [486283, 3, 1, 1, 1, 2, 1, 3, 1, 1],
 [1084584, 5, 4, 4, 9, 2, 10, 5, 6, 1],
 [1108370, 9, 5, 8, 1, 2, 3, 2, 1, 5],
 [1365328, 1, 1, 2, 1, 2, 1, 2, 1, 1],
 [183936, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1223282, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1301945, 5, 1, 1, 1, 1, 1, 1, 1, 1],
 [830690, 5, 2, 2, 2, 3, 1, 1, 3, 1],
 [1117152, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [1110524, 10, 5, 5, 6, 8, 8, 7, 1, 1],
 [1277792, 4, 1, 1, 1, 2, 1, 1, 1, 1],
 [1318671, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [756136, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1142706, 5, 10, 10, 10, 6, 10, 6, 5, 2],
 [1285722, 4, 1, 1, 3, 2, 1, 1, 1, 1],
 [736150, 10, 4, 3, 10, 3, 10, 7, 1, 2],
 [740492, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1204242, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [877291, 6, 10, 10, 10, 10, 10, 8, 10, 10],
 [807657, 6, 1, 3, 2, 2, 1, 1, 1, 1],
 [616240, 5, 3, 4, 3, 4, 5, 4, 7, 1],
 [255644, 10, 5, 8, 10, 3, 10, 5, 1, 3],
 [685977, 5, 3, 4, 1, 4, 1, 3, 1, 1],
 [1050670, 10, 7, 7, 6, 4, 10, 4, 1, 2],
 [1170945, 3, 1, 1, 1, 1, 1, 2, 1, 1],
 [76389, 10, 4, 7, 2, 2, 8, 6, 1, 1],
 [1113038, 8, 2, 4, 1, 5, 1, 5, 4, 4],
 [1108449, 5, 3, 3, 4, 2, 4, 3, 4, 1],
 [846832, 3, 4, 5, 3, 7, 3, 4, 6, 1],
 [1119189, 5, 8, 9, 4, 3, 10, 7, 1, 1],
 [1100524, 6, 10, 10, 2, 8, 10, 7, 3, 3],
 [1169049, 7, 3, 4, 4, 3, 3, 3, 2, 7],
 [1321942, 5, 1, 1, 1, 2, 1, 3, 1, 1],
 [1145420, 6, 1, 1, 1, 2, 1, 2, 1, 1],
 [1224329, 1, 1, 1, 2, 2, 1, 3, 1, 1],
 [1298416, 10, 6, 6, 2, 4, 10, 9, 7, 1],
 [1198641, 10, 10, 6, 3, 3, 10, 4, 3, 2],
 [1049815, 4, 1, 1, 1, 2, 1, 3, 1, 1],
 [734111, 1, 1, 1, 3, 2, 3, 1, 1, 1],
 [850831, 2, 7, 10, 10, 7, 10, 4, 9, 4],
 [1246562, 10, 2, 2, 1, 2, 6, 1, 1, 2],
 [1211594, 3, 1, 1, 1, 1, 1, 2, 1, 1],
 [1368273, 1, 1, 1, 1, 2, 1, 1, 1, 1],
 [1241035, 7, 8, 3, 7, 4, 5, 7, 8, 2],
 [1276091, 6, 1, 1, 3, 2, 1, 1, 1, 1],
 [1182404, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [144888, 8, 10, 10, 8, 5, 10, 7, 8, 1],
 [1035283, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [1313982, 4, 3, 1, 1, 2, 1, 4, 8, 1],
 [1324572, 5, 1, 1, 1, 2, 1, 2, 2, 1],
 [832226, 3, 4, 4, 10, 5, 1, 3, 3, 1],
 [1239967, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1022257, 2, 1, 1, 1, 2, 1, 1, 1, 1],
 [1105524, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [785208, 5, 4, 6, 6, 4, 10, 4, 3, 1],
 [434518, 3, 1, 1, 1, 2, 1, 2, 1, 1],
 [1116192, 1, 1, 1, 1, 2, 1, 2, 1, 1],
 [1371026, 5, 10, 10, 10, 4, 10, 5, 6, 3],
 [95719, 6, 10, 10, 10, 8, 10, 7, 10, 7],
 [1184184, 1, 1, 1, 1, 2, 5, 1, 1, 1],
 [145447, 8, 4, 4, 1, 2, 9, 3, 3, 1],
 [1216947, 1, 1, 1, 1, 2, 1, 3, 1, 1],
 [1350423, 5, 10, 10, 8, 5, 5, 7, 10, 1],
 [1177512, 1, 1, 1, 1, 10, 1, 1, 1, 1],
 [869828, 1, 1, 1, 1, 1, 1, 3, 1, 1],
 [1054593, 10, 5, 5, 3, 6, 7, 7, 10, 1],
 [1181685, 1, 1, 2, 1, 2, 1, 2, 1, 1],
 [369565, 4, 1, 1, 1, 3, 1, 1, 1, 1],
 [1313325, 4, 10, 4, 7, 3, 10, 9, 10, 1],
 [1136142, 2, 1, 1, 1, 3, 1, 2, 1, 1]]
