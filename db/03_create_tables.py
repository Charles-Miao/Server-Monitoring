import pymysql

db=pymysql.connect("192.168.80.129","root","241668Miao","server_information")

cursor=db.cursor()

sql="""CREATE TABLE SYSTEM_SUMMARY (
	   IP CHAR(16) NOT NULL PRIMARY KEY,
	   MODEL CHAR(21),
	   HOST_NAME CHAR(33),
	   MEMORY INT,
	   CPU TEXT,
	   OS_NAME TEXT,
	   OS_VERSION TEXT,
	   BOOTUP_TIME DATETIME )"""


cursor.execute(sql)

sql="""CREATE TABLE CMOS_BATTERY (
	   IP CHAR(16) NOT NULL,
	   HEALTH CHAR(5),
	   STATUS CHAR(5),
	   READING CHAR(5),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE FANS (
	   IP CHAR(16) NOT NULL,
	   MAIN_SYSTEM_CHASSIS CHAR(5),
	   REDUNDANCY CHAR(5),
	   FAN1_STATUS CHAR(5),
	   FAN2_STATUS CHAR(5),
	   FAN3_STATUS CHAR(5),
	   FAN4_STATUS CHAR(5),
	   FAN5_STATUS CHAR(5),
	   FAN6_STATUS CHAR(5),
	   FAN7_STATUS CHAR(5),
	   FAN8_STATUS CHAR(5),
	   FAN9_STATUS CHAR(5),
	   FAN10_STATUS CHAR(5),
	   FAN11_STATUS CHAR(5),
	   FAN12_STATUS CHAR(5),
	   FAN13_STATUS CHAR(5),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE MEMORY (
	   IP CHAR(16) NOT NULL,
	   HEALTH CHAR(5),
	   SLOTS_AVAILABLE INT,
	   SLOTS_USED INT,
	   DIMM1_STATUS CHAR(5),
	   DIMM2_STATUS CHAR(5),
	   DIMM3_STATUS CHAR(5),
	   DIMM4_STATUS CHAR(5),
	   DIMM5_STATUS CHAR(5),
	   DIMM6_STATUS CHAR(5),
	   DIMM7_STATUS CHAR(5),
	   DIMM8_STATUS CHAR(5),
	   DIMM9_STATUS CHAR(5),
	   DIMM10_STATUS CHAR(5),
	   DIMM11_STATUS CHAR(5),
	   DIMM12_STATUS CHAR(5),
	   DIMM13_STATUS CHAR(5),
	   DIMM14_STATUS CHAR(5),
	   DIMM15_STATUS CHAR(5),
	   DIMM16_STATUS CHAR(5),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE NICS (
	   IP CHAR(16) NOT NULL,
	   TOTAL INT,
	   IP1 CHAR(16),
	   IP2 CHAR(16),
	   IP3 CHAR(16),
	   IP4 CHAR(16),
	   IP5 CHAR(16),
	   IP6 CHAR(16),
	   IP7 CHAR(16),
	   IP8 CHAR(16),
	   IP9 CHAR(16),
	   IP10 CHAR(16),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE CPU (
	   IP CHAR(16) NOT NULL,
	   HEALTH CHAR(5),
	   CPU1_STATUS CHAR(5),
	   CPU2_STATUS CHAR(5),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE TEMPS (
	   IP CHAR(16) NOT NULL,
	   MAIN_SYSTEM_CHASSIS CHAR(5),
	   STATUS CHAR(5),
	   READING INT,
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE POWER_SUPPLIES (
	   IP CHAR(16) NOT NULL,
	   MAIN_SYSTEM_CHASSIS CHAR(5),
	   REDUNDANCY CHAR(5),
	   PS1_STATUS CHAR(5),
	   PS2_STATUS CHAR(5),
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE VIRTUAL_DISK (
	   IP CHAR(16) NOT NULL,
	   VD1_STATUS CHAR(5),
	   VD1_STATE CHAR(6),
	   VD1_RAID CHAR(5),
	   VD1_SIZE INT,
	   VD2_STATUS CHAR(5),
	   VD2_STATE CHAR(6),
	   VD2_RAID CHAR(5),
	   VD2_SIZE INT,
	   VD3_STATUS CHAR(5),
	   VD3_STATE CHAR(6),
	   VD3_RAID CHAR(5),
	   VD3_SIZE INT,
	   VD4_STATUS CHAR(5),
	   VD4_STATE CHAR(6),
	   VD4_RAID CHAR(5),
	   VD4_SIZE INT,
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

sql="""CREATE TABLE PHYSICAL_DISKS (
	   IP CHAR(16) NOT NULL,
	   PD1_STATUS CHAR(5),
	   PD1_STATE CHAR(6),
	   PD1_SIZE INT,
	   PD2_STATUS CHAR(5),
	   PD2_STATE CHAR(6),
	   PD2_SIZE INT,
	   PD3_STATUS CHAR(5),
	   PD3_STATE CHAR(6),
	   PD3_SIZE INT,
	   PD4_STATUS CHAR(5),
	   PD4_STATE CHAR(6),
	   PD4_SIZE INT,
	   PD5_STATUS CHAR(5),
	   PD5_STATE CHAR(6),
	   PD5_SIZE INT,
	   PD6_STATUS CHAR(5),
	   PD6_STATE CHAR(6),
	   PD6_SIZE INT,
	   PD7_STATUS CHAR(5),
	   PD7_STATE CHAR(6),
	   PD7_SIZE INT,
	   PD8_STATUS CHAR(5),
	   PD8_STATE CHAR(6),
	   PD8_SIZE INT,
	   PD9_STATUS CHAR(5),
	   PD9_STATE CHAR(6),
	   PD9_SIZE INT,
	   PD10_STATUS CHAR(5),
	   PD10_STATE CHAR(6),
	   PD10_SIZE INT,
	   PD11_STATUS CHAR(5),
	   PD11_STATE CHAR(6),
	   PD11_SIZE INT,
	   PD12_STATUS CHAR(5),
	   PD12_STATE CHAR(6),
	   PD12_SIZE INT,
	   PD13_STATUS CHAR(5),
	   PD13_STATE CHAR(6),
	   PD13_SIZE INT,
	   PD14_STATUS CHAR(5),
	   PD14_STATE CHAR(6),
	   PD14_SIZE INT,
	   PD15_STATUS CHAR(5),
	   PD15_STATE CHAR(6),
	   PD15_SIZE INT,
	   PD16_STATUS CHAR(5),
	   PD16_STATE CHAR(6),
	   PD16_SIZE INT,
	   PD17_STATUS CHAR(5),
	   PD17_STATE CHAR(6),
	   PD17_SIZE INT,
	   PD18_STATUS CHAR(5),
	   PD18_STATE CHAR(6),
	   PD18_SIZE INT,
	   PD19_STATUS CHAR(5),
	   PD19_STATE CHAR(6),
	   PD19_SIZE INT,
	   PD20_STATUS CHAR(5),
	   PD20_STATE CHAR(6),
	   PD20_SIZE INT,
	   PD21_STATUS CHAR(5),
	   PD21_STATE CHAR(6),
	   PD21_SIZE INT,
	   PD22_STATUS CHAR(5),
	   PD22_STATE CHAR(6),
	   PD22_SIZE INT,
	   PD23_STATUS CHAR(5),
	   PD23_STATE CHAR(6),
	   PD23_SIZE INT,
	   PD24_STATUS CHAR(5),
	   PD24_STATE CHAR(6),
	   PD24_SIZE INT,
	   PD25_STATUS CHAR(5),
	   PD25_STATE CHAR(6),
	   PD25_SIZE INT,
	   PD26_STATUS CHAR(5),
	   PD26_STATE CHAR(6),
	   PD26_SIZE INT,
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

db.close()