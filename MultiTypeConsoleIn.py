#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
# ver. 1.21117
# (C) 2012 Matsuda Hiroaki

"""
 \file MultiTypeConsoleIn.py
 \brief This component it is possible to output a pseudo signal of any data type
 \date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import ConfigPaser for read inifile
import ConfigParser as Conf
import csvreader
import time

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
multitypeconsolein_spec = ["implementation_id", "MultiTypeConsoleIn", 
		 "type_name",         "MultiTypeConsoleIn", 
		 "description",       "This component it is possible to output a pseudo signal of any data type", 
		 "version",           "1.0.0", 
		 "vendor",            "Matsuda Hiroaki", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "0", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

class MultiTypeConsoleIn(OpenRTM_aist.DataFlowComponentBase):
	
	"""
	\class MultiTypeConsoleIn
	\brief This component it is possible to output a pseudo signal of any data type
	
	"""

	def __init__(self, manager):
		"""
		\brief constructor
		\param manager Maneger Object
		"""
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		# Read ini file	
		self.conf = Conf.SafeConfigParser()
                self.conf.read('ini\multitypeconsolein.ini')
		
                self.num = int(self.conf.get('DATA', 'num'))
		self.type = self.conf.get('DATA', 'type')
		self.mode = self.conf.get('DATA', 'mode')
		self.loop = int(self.conf.get('DATA', 'loop'))
		self.wait = self.conf.get('DATA', 'wait')

		self.flag = 'none'
		if self.type.find('Seq') > 0:
			self.flag = 'Seq'
		
		if self.type == 'TimedShort':
			self._d_data = RTC.TimedShort(RTC.Time(0,0),0)
		
		elif self.type == 'TimedShortSeq':
			self._d_data = RTC.TimedShortSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedUShort':
			self._d_data = RTC.TimedUShort(RTC.Time(0,0),0)
		
		elif self.type == 'TimedUShortSeq':
			self._d_data = RTC.TimedUShortSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedLong':
			self._d_data = RTC.TimedLong(RTC.Time(0,0),0)
		
		elif self.type == 'TimedLongSeq':
			self._d_data = RTC.TimedLongSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedULong':
			self._d_data = RTC.TimedULong(RTC.Time(0,0),0)
		
		elif self.type == 'TimedULongSeq':
			self._d_data = RTC.TimedULongSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedFloat':
			self._d_data = RTC.TimedFloat(RTC.Time(0,0),0)
		
		elif self.type == 'TimedFloatSeq':
			self._d_data = RTC.TimedFloatSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedDouble':
			self._d_data = RTC.TimedDouble(RTC.Time(0,0),0)
		
		elif self.type == 'TimedDoubleSeq':
			self._d_data = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedString':
			self._d_data = RTC.TimedString(RTC.Time(0,0),0)
		
		elif self.type == 'TimedStringSeq':
			self._d_data = RTC.TimedStringSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedWString':
			self._d_data = RTC.TimedWString(RTC.Time(0,0),0)
		
		elif self.type == 'TimedWStringSeq':
			self._d_data = RTC.TimedWStringSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedChar':
			self._d_data = RTC.TimedChar(RTC.Time(0,0),0)
		
		elif self.type == 'TimedCharSeq':
			self._d_data = RTC.TimedCharSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedWChar':
			self._d_data = RTC.TimedWChar(RTC.Time(0,0),0)
		
		elif self.type == 'TimedWCharSeq':
			self._d_data = RTC.TimedWCharSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedOctet':
			self._d_data = RTC.TimedOctet(RTC.Time(0,0),0)
		
		elif self.type == 'TimedOctetSeq':
			self._d_data = RTC.TimedOctetSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedBool':
			self._d_data = RTC.TimedBool(RTC.Time(0,0),0)
		
		elif self.type == 'TimedBoolSeq':
			self._d_data = RTC.TimedBoolSeq(RTC.Time(0,0),[])

		else:
			print('The specified type did not mutch.Please check multitypeconsolein.ini')
			
		self._dataOut = OpenRTM_aist.OutPort("data", self._d_data)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>
		 
	def onInitialize(self):
		"""
		
		The initialize action (on CREATED->ALIVE transition)
		formaer rtc_init_entry() 
		
		\return RTC::ReturnCode_t
		
		"""
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		self.addOutPort("data",self._dataOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		print('OnInitialize')

                # Read CSV file
		self.csvfile = csvreader.CsvReader('ini/multitypeconsolein.ini')
		self.csv_path = self.csvfile.get_csv_path()
		
		return RTC.RTC_OK
	
	def onFinalize(self, ec_id):
		"""
	
		The finalize action (on ALIVE->END transition)
		formaer rtc_exiting_entry()
	
		\return RTC::ReturnCode_t
	
		"""
		
		print('OnFinalize')
	
		return RTC.RTC_OK
	
	def onActivated(self, ec_id):
		"""
	
		The activated action (Active state entry action)
		former rtc_active_entry()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		
		print('OnActivated')
	
		return RTC.RTC_OK
	
	def onDeactivated(self, ec_id):
		"""
	
		The deactivated action (Active state exit action)
		former rtc_active_exit()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		print('OnDeactivated')
	
		return RTC.RTC_OK
	
	def onExecute(self, ec_id):
		"""
	
		The execution action that is invoked periodically
		former rtc_active_do()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		self.mode = self.conf.get('DATA', 'mode')
		
		if self.mode == 'csv':
			if self.flag != 'Seq':
				raise ValueError('Using CSV mode, Must be set to the data type of port Seq type')

			print('Plser input write csvfile number :ex. csv_1')
			csv_number = str(sys.stdin.readline())
			csv_number = int(csv_number.split('_')[1])
			csv_list = self.csvfile.read_csv(self.csv_path[csv_number - 1])
			
			for i in range(self.loop):		
				for row in csv_list:
					self._d_data.data = row
					OpenRTM_aist.setTimestamp(self._d_data)
					print 'Sending to subscriver: ', self._d_data.data
					print('Time stamp: %f[s] %f[ns]' %(self._d_data.tm.sec, self._d_data.tm.nsec))
					self._dataOut.write()
		
		elif self.mode == 'console':			
			if self.flag == 'none':
				print ('Plese input type of %s variable :' %self.type)
				if self.type.find('Short') > 0:
					data = int(sys.stdin.readline())
			
				elif self.type.find('Long') > 0:
					data = long(sys.stdin.readline())
				
				elif self.type.find('Float') > 0:
					data = float(sys.stdin.readline())
				
				elif self.type.find('Double') > 0:
					data = float(sys.stdin.readline())
			
				elif self.type.find('Char') > 0:
					data = int(sys.stdin.readline())
				
				elif self.type.find('String') > 0:
					data = str(sys.stdin.readline())
			
				elif self.type.find('Bool') > 0:
					data = bool(sys.stdin.readline())
			
				elif self.type.find('Octet') > 0:
					data = int(sys.stdin.readline())
			
			elif self.flag == 'Seq':
				data = []	
				for i in range(self.num):
					print ('Plese input type of  %s variable %d of %d :' %(self.type, i + 1, self.num))
				
					if self.type.find('Short') > 0:
						data.append(int(sys.stdin.readline()))
			
					elif self.type.find('Long') > 0:
						data.append(long(sys.stdin.readline()))
				
					elif self.type.find('Float') > 0:
						data.append(float(sys.stdin.readline()))
			
					elif self.type.find('Double') > 0:
						data.append(float(sys.stdin.readline()))
			
					elif self.type.find('Char') > 0:
						data.append(int(sys.stdin.readline()))
				
					elif self.type.find('String') > 0:
						data.append(str(sys.stdin.readline()))
			
					elif self.type.find('Bool') > 0:
						data.append(bool(sys.stdin.readline()))
			
					elif self.type.find('Octet') > 0:
						data.append(int(sys.stdin.readline()))
					
			self._d_data.data = data

			OpenRTM_aist.setTimestamp(self._d_data)
			print 'Sending to subscriver: ', self._d_data.data
			print('Time stamp: %f[s] %f[ns]' %(self._d_data.tm.sec, self._d_data.tm.nsec))
			self._dataOut.write()
			time.sleep(self.wait * 0.001)
	
		return RTC.RTC_OK	

def MultiTypeConsoleInInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=multitypeconsolein_spec)
    manager.registerFactory(profile,
                            MultiTypeConsoleIn,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MultiTypeConsoleInInit(manager)

    # Create a component
    comp = manager.createComponent("MultiTypeConsoleIn")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

