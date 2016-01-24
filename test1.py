from WindPy import w
w.start()
tmp = w.wsd('150018.SZ', 'close', '2015-1-1', '2015-12-31')
print tmp.Data