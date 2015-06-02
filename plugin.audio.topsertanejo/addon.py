import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')


url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/fernandosorocabaprevisodotempos.mp3'
li = xbmcgui.ListItem('Fernando & Sorocaba - Previsao Do Tempo', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/jorgemateusosanjoscantams.mp3'
li = xbmcgui.ListItem('Jorge & Mateus - Os Anjos Cantam', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/hugotiagojoonetofredericoelamelhorquevoc.mp3'
li = xbmcgui.ListItem('Hugo & Tiago & Joao Neto & Frederico - Ela e Melhor Que Voce', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/victorlohenriquejuliano10minutoslongedevocs.mp3'
li = xbmcgui.ListItem('Victor & Leo & Henrique & Juliano - 10 Minutos Longe De Voce', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/lutchelobrunomarronepirandodenovos.mp3'
li = xbmcgui.ListItem('Joao Neto & Frederico & Gregory & Gabriel - Presto Pouco', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/edsonviniciusthiagobravafeinhos.mp3'
li = xbmcgui.ListItem('Edson & Vinicius & Thiago Brava - Feinho', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/thiagobravanamorabobos.mp3'
li = xbmcgui.ListItem('Thiago Brava - Namora Bobo', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/thaemethiagofernandosorocabaoqueacontecenabaladas.mp3'
li = xbmcgui.ListItem('Thaeme & Thiago & Fernando & Sorocaba - O Que Acontece Na Balada', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/lucasluccovaivendos.mp3'
li = xbmcgui.ListItem('Lucas Lucco - Vai Vendo', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/cristianoarajohojeeutterrvels.mp3'
li = xbmcgui.ListItem('Lucas Lucco - Hoje Eu To Terrivel', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/cristianoarajohojeeutterrvels.mp3'
li = xbmcgui.ListItem('Bruninho & Davi - Fico Com Voce', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/pedropauloalexlokalokas.mp3'
li = xbmcgui.ListItem('Pedro Paulo & Alex - Loka Loka', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/0_munhozmarianoseubombeiros.mp3'
li = xbmcgui.ListItem('Munhoz & Mariano - Seu Bombeiro', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/thiagogracianoseeufossericos.mp3'
li = xbmcgui.ListItem('Thiago & Graciano - Se Eu Fosse Rico', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/maurcioeduardochavequeiros.mp3'
li = xbmcgui.ListItem('Mauricio & Eduardo - Chavequeiro', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://www.paradaosertanejo.com.br/arquivos/parada_artista/clebercauanwesleysafadosolteirodesapegado.mp3'
li = xbmcgui.ListItem('Cleber & Cauan & Wesley Safadao - Solteiro Desapegado', iconImage='')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)