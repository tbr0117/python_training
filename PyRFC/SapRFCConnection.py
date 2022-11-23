from pyrfc import Connection
conn = Connection(ashost='192.***.*.**', sysnr='00', client='300', user='', passwd='')

result = conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!')
print (result)