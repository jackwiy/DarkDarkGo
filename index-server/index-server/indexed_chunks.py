#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    query_processing.py - Matches the query against the saved indexed chunks and returns a list of dictionaries with docID
    author: Nayeem Aquib
    email: nayeemaquib@bennington.edu
    date: 12/1/2017

"""
from bs4 import BeautifulSoup


sample_indexed_chunks_dict = {"'s": {'doc_id': {'0': [6, 39]}, 'word_count': 2},
 '.onion': {'doc_id': {'4': [4, 27]}, 'word_count': 2},
 '//dirnxxdraygbifgc.onion/': {'doc_id': {'0': [25]}, 'word_count': 1},
 '10years.debconf.org': {'doc_id': {'4': [27]}, 'word_count': 1},
 'ammo': {'doc_id': {'4': [3, 9, 19, 25]}, 'word_count': 4},
 'android': {'doc_id': {'0': [24]}, 'word_count': 1},
 'back': {'doc_id': {'0': [10]}, 'word_count': 1},
 'backends': {'doc_id': {'4': [23]}, 'word_count': 1},
 'bank': {'doc_id': {'3': [9]}, 'word_count': 1},
 'become': {'doc_id': {'2': [8, 34]}, 'word_count': 2},
 'best': {'doc_id': {'3': [7]}, 'word_count': 1},
 'biggest': {'doc_id': {'4': [2, 25]}, 'word_count': 2},
 'bitcoi': {'doc_id': {'2': [22]}, 'word_count': 1},
 'bitcoin': {'doc_id': {'0': [1, 5, 8, 28, 31]}, 'word_count': 5},
 'bitcoins': {'doc_id': {'0': [13]}, 'word_count': 1},
 'bitpharma': {'doc_id': {'4': [0, 23]}, 'word_count': 2},
 'buy': {'doc_id': {'2': [3, 29]}, 'word_count': 2},
 'cannabis': {'doc_id': {'2': [18]}, 'word_count': 1},
 'check': {'doc_id': {'0': [11]}, 'word_count': 1},
 'ci': {'doc_id': {'2': [37]}, 'word_count': 1},
 'citizen': {'doc_id': {'2': [11]}, 'word_count': 1},
 'co': {'doc_id': {'3': [18]}, 'word_count': 1},
 'cocai': {'doc_id': {'0': [47]}, 'word_count': 1},
 'cocaine': {'doc_id': {'0': [14], '4': [8]}, 'word_count': 2},
 'counterfeit': {'doc_id': {'3': [8]}, 'word_count': 1},
 'counterfeits': {'doc_id': {'3': [5]}, 'word_count': 1},
 'darkweb': {'doc_id': {'0': [5, 38]}, 'word_count': 2},
 'debian': {'doc_id': {'4': [13]}, 'word_count': 1},
 'dedope': {'doc_id': {'2': [0, 24]}, 'word_count': 2},
 'deep': {'doc_id': {'0': [15]}, 'word_count': 1},
 'device': {'doc_id': {'0': [20]}, 'word_count': 1},
 'drug': {'doc_id': {'0': [1, 9, 27, 34, 42], '4': [5, 28]}, 'word_count': 7},
 'easycoin': {'doc_id': {'0': [0, 30]}, 'word_count': 2},
 'etc': {'doc_id': {'0': [25]}, 'word_count': 1},
 'euro': {'doc_id': {'3': [4, 17]}, 'word_count': 2},
 'europe': {'doc_id': {'3': [12]}, 'word_count': 1},
 'european': {'doc_id': {'4': [3, 26]}, 'word_count': 2},
 'fake': {'doc_id': {'2': [6, 19]}, 'word_count': 2},
 'free': {'doc_id': {'0': [4]}, 'word_count': 1},
 'für': {'doc_id': {'2': [11, 21]}, 'word_count': 2},
 'german': {'doc_id': {'2': [2]}, 'word_count': 1},
 'get': {'doc_id': {'2': [4, 17]}, 'word_count': 2},
 'guns': {'doc_id': {'4': [1, 7, 17, 23]}, 'word_count': 4},
 'heroin': {'doc_id': {'0': [22]}, 'word_count': 1},
 'hidden': {'doc_id': {'0': [18]}, 'word_count': 1},
 'high': {'doc_id': {'3': [2, 15]}, 'word_count': 2},
 'hqer': {'doc_id': {'3': [0, 13]}, 'word_count': 2},
 'http': {'doc_id': {'0': [23]}, 'word_count': 1},
 'identity': {'doc_id': {'2': [1, 11, 14, 24]}, 'word_count': 4},
 'iphone': {'doc_id': {'0': [22]}, 'word_count': 1},
 'kaufen': {'doc_id': {'2': [8, 16, 20]}, 'word_count': 3},
 'laundry': {'doc_id': {'0': [9]}, 'word_count': 1},
 'list': {'doc_id': {'4': [6]}, 'word_count': 1},
 'location': {'doc_id': {'0': [16]}, 'word_count': 1},
 'maintainance': {'doc_id': {'0': [5]}, 'word_count': 1},
 'manage': {'doc_id': {'0': [11]}, 'word_count': 1},
 'marijuana': {'doc_id': {'2': [14]}, 'word_count': 1},
 'mdma': {'doc_id': {'0': [20]}, 'word_count': 1},
 'mixer': {'doc_id': {'0': [6]}, 'word_count': 1},
 'n/a': {'doc_id': {'0': [0]}, 'word_count': 1},
 'new': {'doc_id': {'2': [10, 23]}, 'word_count': 2},
 'notes': {'doc_id': {'3': [10]}, 'word_count': 1},
 'ns': {'doc_id': {'2': [23]}, 'word_count': 1},
 'onion': {'doc_id': {'2': [0, 13]}, 'word_count': 2},
 'onion.debian.org': {'doc_id': {'4': [0, 1, 2]}, 'word_count': 3},
 'onionbalance': {'doc_id': {'4': [25]}, 'word_count': 1},
 'oniondir': {'doc_id': {'0': [12]}, 'word_count': 1},
 'online': {'doc_id': {'0': [27]}, 'word_count': 1},
 'passport': {'doc_id': {'2': [7, 20]}, 'word_count': 2},
 'passports': {'doc_id': {'2': [1, 6, 15, 19, 24, 27, 32]}, 'word_count': 7},
 'pay': {'doc_id': {'0': [30]}, 'word_count': 1},
 'peoples': {'doc_id': {'0': [0, 26, 33]}, 'word_count': 3},
 'prescriptions': {'doc_id': {'4': [16]}, 'word_count': 1},
 'privacy': {'doc_id': {'4': [3]}, 'word_count': 1},
 'project': {'doc_id': {'4': [14]}, 'word_count': 1},
 'psychedelics': {'doc_id': {'4': [12]}, 'word_count': 1},
 'quality': {'doc_id': {'3': [3, 16]}, 'word_count': 2},
 'real': {'doc_id': {'2': [4, 23, 30]}, 'word_count': 3},
 'run': {'doc_id': {'4': [10]}, 'word_count': 1},
 'search': {'doc_id': {'1': [3, 8]}, 'word_count': 2},
 'served': {'doc_id': {'4': [20]}, 'word_count': 1},
 'service': {'doc_id': {'0': [19]}, 'word_count': 1},
 'services': {'doc_id': {'2': [2, 15]}, 'word_count': 2},
 'several': {'doc_id': {'4': [22]}, 'word_count': 1},
 'shop': {'doc_id': {'2': [4]}, 'word_count': 1},
 'site': {'doc_id': {'0': [1]}, 'word_count': 1},
 'speed': {'doc_id': {'0': [16]}, 'word_count': 1},
 'sto': {'doc_id': {'4': [29]}, 'word_count': 1},
 'store': {'doc_id': {'0': [2, 28, 35], '4': [6]}, 'word_count': 4},
 'supplier': {'doc_id': {'0': [10, 43]}, 'word_count': 2},
 'today': {'doc_id': {'2': [12, 25]}, 'word_count': 2},
 'tor': {'doc_id': {'4': [0]}, 'word_count': 1},
 'torch': {'doc_id': {'1': [0, 5]}, 'word_count': 2},
 'uk': {'doc_id': {'2': [0, 5, 10, 26, 31, 36]}, 'word_count': 6},
 'untill': {'doc_id': {'0': [7]}, 'word_count': 1},
 'using': {'doc_id': {'4': [24]}, 'word_count': 1},
 'viagra': {'doc_id': {'4': [20]}, 'word_count': 1},
 'wall': {'doc_id': {'0': [32]}, 'word_count': 1},
 'wallet': {'doc_id': {'0': [2, 29]}, 'word_count': 2},
 'web': {'doc_id': {'0': [16]}, 'word_count': 1},
 'websites': {'doc_id': {'0': [21]}, 'word_count': 1},
 'weed': {'doc_id': {'2': [3, 6, 10]}, 'word_count': 3},
 'xtc': {'doc_id': {'0': [18]}, 'word_count': 1}}

sample_content_chunk = [{'doc_id': 0,
  'html': 'Site is down for maintainance.<br>\r\n<br>\r\nUntill we are back check OnionDir for other Deep Web Tor hidden service .onion websites:<br>\r\n<br>\r\n<a href="http://dirnxxdraygbifgc.onion/">http://dirnxxdraygbifgc.onion/</a>',
  'link': 'http://6w6vcynl6dumn67c.onion',
  'title': 'N/A'},
 {'doc_id': 1,
  'html': '',
  'link': 'http://p3igkncehackjtib.onion',
  'title': ''},
 {'doc_id': 2,
  'html': '',
  'link': 'http://54flq67kqr5wvjqf.onion',
  'title': ''},
 {'doc_id': 3,
  'html': '',
  'link': 'http://dppmfxaacucguzpc.onion',
  'title': ''},
 {'doc_id': 4,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="UK Guns and ammo store, buy guns and ammo on the deep web with bitcoin at our Tor store." />\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>UK Guns and Ammo Store - Buy guns and ammo in the UK for Bitcoi',
  'link': 'http://tuu66yxvrnn3of7l.onion',
  'title': 'UK Guns and Ammo Store - Buy guns and ammo in the UK for Bitcoin.'},
 {'doc_id': 0,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="Peoples drug store, the number one deep web drug vendor. Buy drugs with Bitcoin"/>\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>Peoples Drug Store - The Darkweb\'s Best Online Drug Supplier! - Buy cocai',
  'link': 'http://newpdsuslmzqazvr.onion',
  'title': "Peoples Drug Store - The Darkweb's Best Online Drug Supplier! - Buy cocaine, speed, xtc, mdma, heroin and more at peoples drug store, pay with Bitcoin"},
 {'doc_id': 1,
  'html': '<html xmlns="http://www.w3.org/1999/xhtml"> \n<head> \n<title>TORCH: Tor Search!</title> \n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> \n<meta name="description" content=""/> \n<meta name="keywords" content=""/> \n<link rel="shortcut icon" href="favicon.png" type="image/png" />\n \n<style type="text/css"> \nbody{\n\ttext-align: center;\n\tfont-family:Verdana, Arial, Helvetica, sans-serif;\n\tfont-size:.7em;\n\tmargin: 10px;\n\tcolor: #000;\n\tbackground: #fff;\n\tmin-width: 520px;\n}\na{\n\tcolor: #009;\n\tt',
  'link': 'http://xmh57jrzrnw6insl.onion',
  'title': 'TORCH: Tor Search!'},
 {'doc_id': 2,
  'html': 'ns<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="DeDope - Deutscher Weed und Hash Shop, weed online kaufen, weed für bitcoins, marijuana online kaufen, cannabis online kaufen für Bitcoins" />\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>DeDope - ',
  'link': 'http://kbvbh4kdddiha2ht.onion',
  'title': 'DeDope - German Weed Shop - weed online kaufen, weed für bitcoins, marijuana online kaufen, cannabis online kaufen für Bitcoi'},
 {'doc_id': 3,
  'html': '',
  'link': 'http://fogcore5n3ov3tui.onion',
  'title': ''},
 {'doc_id': 4,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="Bitpharma - Cocaine for Bitcoins, Psychedelics for Bitcoins, Prescriptions for Bitcoins, Viagra for Bitcoins"/>\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>BitPharma - biggest european .onion drug sto',
  'link': 'http://s5q54hfww56ov2xc.onion',
  'title': 'BitPharma - biggest european .onion drug store - Cocaine for Bitcoins, Psychedelics for Bitcoins, Prescriptions for Bitcoins, Viagra for Bitcoins'},
 {'doc_id': 0,
  'html': '',
  'link': 'https://www.facebookcorewwwi.onion',
  'title': ''},
 {'doc_id': 1,
  'html': '',
  'link': 'http://xdagknwjc7aaytzh.onion',
  'title': ''},
 {'doc_id': 2,
  'html': '',
  'link': 'http://wvk32thojln4gpp4.onion',
  'title': ''},
 {'doc_id': 3,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="High quality counterfeit euro banknotes for bitcoin - buy fake euros with bitcoin - best quality counterfeits on the deep web"/>\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>HQER - High Quality Euro Co',
  'link': 'http://y3fpieiezy2sin4a.onion',
  'title': 'HQER - High Quality Euro Counterfeits - best counterfeit bank notes in europe'},
 {'doc_id': 4,
  'html': '<!DOCTYPE html>\n <html>\n <head>\n   <meta charset="utf-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width\\=device-width, initial-scale=1">\n   <meta name="author" content="The Tor Project, Inc.">\n   <meta name="description" content="The Tor Project\'s free software protects your privacy online. Site blocked? Email [mailto:gettor@torproject.org] for help downloading Tor Browser.">\n   <meta name="keywords" content="tor, tor project, tor browser, avoid censorsh',
  'link': 'http://expyuzz4wqqyqhjn.onion',
  'title': 'Tor Project | Privacy Online'},
 {'doc_id': 0,
  'html': '',
  'link': 'http://storegsq3o5mfxiz.onion',
  'title': ''},
 {'doc_id': 1,
  'html': '',
  'link': 'http://jvrnuue4bvbftiby.onion',
  'title': ''},
 {'doc_id': 2,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="UKPassports - Buy passport from the United Kingdom UK, real passports from the UK, no fake passports"/>\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>UK Passports - Buy real UK passports, become a UK ci',
  'link': 'http://vfqnd6mieccqyiit.onion',
  'title': 'UK Passports - Buy real UK passports, become a UK citizen now. Our passports are no fake passports, they are real passports.'},
 {'doc_id': 3,
  'html': '',
  'link': 'http://5plvrsgydwy2sgce.onion',
  'title': ''},
 {'doc_id': 4,
  'html': '<!DOCTYPE html>\n<HTML lang="en">\n<HEAD>\n   <TITLE>onion.debian.org</TITLE>\n   <meta charset="UTF-8">\n</HEAD>\n<BODY>\n\n<H1>onion.debian.org</H1>\n\nThis is a list of <a href="https://www.torproject.org/docs/hidden-services">onion services</a>\nrun by the <a href="https://www.debian.org/">Debian project</a>.  Most of them are served\nfrom several backends using\n<a href="https://github.com/DonnchaC/onionbalance">OnionBalance</a>.\n\n<ul>\n\n<li id="10years.debconf.org"><strong>10years.debconf.org</strong>: <a href="',
  'link': 'http://5nca3wxl33tzlzj5.onion',
  'title': 'onion.debian.org'},
 {'doc_id': 0,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="EasyCoin.net is a Bitcoin Wallet and Bitcoin Laundry service, we offer bitcoin laundry without any fees, use on Iphone, Android." />\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>\r\nEasyCoin Bitcoin Wall',
  'link': 'http://easycoinsayj7p5l.onion',
  'title': '\r\nEasyCoin Bitcoin Wallet and free Bitcoin Mixer / Bitcoin Laundry, manage your Bitcoins from any location, from any device: Iphone, Android etc - Online Bitcoin Wallet'},
 {'doc_id': 1,
  'html': '',
  'link': 'http://5mvm7cg6bgklfjtp.onion',
  'title': ''},
 {'doc_id': 2,
  'html': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\r\n<meta name="description" content="Onion Identity Store - buy european fake ids, fake passports with Bitcoin"/>\r\n<link rel="icon" type="image/icon" href="favicon.ico">\t\r\n<link rel="shortcut icon" type="image/icon" href="favicon.ico">\r\n<title>Onion Identity Services - Get your fake passport and a new identity today</titl',
  'link': 'http://abbujjh5vqtq77wg.onion',
  'title': 'Onion Identity Services - Get your fake passport and a new identity today'},
 {'doc_id': 3,
  'html': '',
  'link': 'http://lw4ipk5choakk5ze.onion',
  'title': ''},
 {'doc_id': 4,
  'html': '',
  'link': 'http://e2qizoerj4d6ldif.onion',
  'title': ''}]

key_docs = [k['doc_id'] for k in sample_content_chunk if k.get('doc_id')]
N = len(key_docs)

print(N)


def snippet_builder(doc_ID):
    if doc_ID in key_docs:
        a = search_list_of_dict(doc_ID, sample_content_chunk)
        snippet = {}
        soup = BeautifulSoup(a['html'])
        s = soup.getText()
        desc = s[1:300]
        snippet['title'] = a['title']
        snippet['href'] = a['link']
        snippet['desc'] = desc + '...'
        return snippet


def search_list_of_dict(doc_ID, content_chunk_list):
    for item in content_chunk_list:
        if item['doc_ID'] == doc_ID:
            return item

