import json
# import requests

progs = [
  {
      'title': 'arthurs day out',
      'desc': """A fun text adventure created for the PunyInform game jam.
Tons of fun pop culture references.
My first adventure game.
Take Arthur out for the day and explore the town!""",
      'category': 'game',
      'author': 'WauloK'
  },
  {
      'title': 'blaster',
      'desc': """This is my winning entry into Shallan's August 2021 compo. It was built using TRSE and XEMU and most certainly has 'War Hawk' undertones...

It uses 8 x 16 pixel wide sprites (16 colours available for each sprite) and 80 column mode. Bullets are generated using characters.""",
      'category': 'game',
      'author': 'geehaf'
  },
  {
      'title': 'camelot-1536dots',
      'desc': """1536 dots in 60fps by Camelot

Load & run in C65 mode. Tested on DevKit and Xemu.""",
      'category': 'demo',
      'author': 'JesperGravgaard'
  },
  {
      'title': 'charwars65',
      'desc': 'My entry for Shallan\'s Basic Challenge in Feb 21.',
      'category': 'game',
      'author': 'hstampfl'
  },
  {
      'title': 'cheek2cheek',
      'desc': 'An example of using BASIC 65\'s PLAY command to play non-blocking polyphonic music.',
      'category': 'music',
      'author': 'gurce'
  },
  {
      'title': 'chicko',
      'desc': """A simple jumping game in the style of Chrome's 'Dino' which was submitted for Shallan's April 2021 Mega 65 competition.""",
      'category': 'game',
      'author': 'geehaf'
  },
  {
      'title': 'colours',
      'desc': """Simple Colour Demo.

Just playing around with colours a bit. Maybe someday I'll add some colour cycling.""",
      'category': 'demo',
      'author': 'ubik'
  },
  {
      'title': 'combat',
      'desc': """Small 2 players game written in Basic V10 and tested/working on XEMU - 911001.BIN ROM (Shallan monthly give away challenge)
This game is a partial clone of Atari 2600 game 'COMBAT'.
d81 files contains a version without comments (COMBAT_NO_CMT.prg) and a version with comments (COMBAT_CMT.prg).""",
      'category': 'game',
      'author': 'Amok64'
  },
  {
      'title': 'guide akmafin',
      'desc': 'A Game for the MEGA65 (Labyrinth/Maze)',
      'category': 'game',
      'author': 'stepz'
  },
  {
      'title': 'hiomill65',
      'desc': """A port of the 2020 4K Compo entry Hose It Out. Graphics are updated from the C128 VDC version. So it runs in 320x200 256 colour mode. Although the graphics currently only use 16 of said 256 colour mode.
Joystick in port 2. In some emuators the sprite is off by a couple of pixels, in others it right. Needs 'merger' branch or hardware to get the C64 sprite working properly.""",
      'category': 'game',
      'author': 'oziphantom'
  },
  {
      'title': 'hitblock65',
      'desc': """A small demake of PC game HitBlock (a remake of C64 game Crillion).

Full project for C64Studio. GitHub repo is at: https://github.com/GeorgRottensteiner/HitBlock-Mega65""",
      'category': 'game',
      'author': 'Endurion'
  },
  {
      'title': 'hopalong',
      'desc': 'Hopalong fractal demo for MEGA65.',
      'category': 'demo',
      'author': 'ubik'
  },
  {
      'title': 'lemonade65',
      'desc': """Since no 8-bit-platform is complete without its own implementation of the good old lemonade stand simulation, I decided to bring the good old PET game over to our beloved platform.
The C65/Mega65 version is (of course ;)) a little souped up: It's a 2 player game, we have a high score list and a fancy report graph after the sale.""",
      'category': 'game',
      'author': 'ubik'
  },
  {
      'title': 'kalle65',
      'desc': 'Kalle Kloakk Mega 65',
      'category': 'game',
      'author': 'Docster'
  },
  {
      'title': 'led-designer',
      'desc': 'MEGA65 Power LED Colour Designer.',
      'category': 'utility',
      'author': 'ubik'
  },
  {
      'title': 'logitrumps',
      'desc': 'quiz game entry in Shallan\'s Basic Challenge',
      'category': 'game',
      'author': 'Martin Roscher'
  },
  {
      'title': 'kkniffel',
      'desc': 'Yahtzee style game for the MEGA65. Includes (actually reasonably skillful) computer player, high score list and session counter to monitor your KKniffel addiction.',
      'category': 'game',
      'author': 'ubik'
  },
  {
      'title': 'manche',
      'desc': """A MOD 'Replayer' for your MEGA65! Reads files from the SD card.

Most first generation MODs now supported.

Usage:
- Place .MOD files onto your SD Card
- Run Manche
- Press F1 and type in your .MOD file name and press ENTER to play. More detailed instructions can be found within .zip file at:
  https://files.mega65.org?id=41df2383-3001-4b90-a499-7001721cfe5d""",
      'category': 'utility',
      'author': 'M3wP'
  },
  {
      'title': 'mand65',
      'desc': """Started out as a benchmark tool for the computational power of the MEGA65 and aims to be a mandelbrot fractal explorer soon!

For now it just can draw a basic mandelbrot set.

Source code available at https://github.com/lydon42/mandelbrot-explorer65""",
      'category': 'utility',
      'author': 'lydon'
  },
  {
      'title': 'megadots',
      'desc': """A platformer game (Jump&Run)

  code: https://github.com/jaammees/megadots""",
      'category': 'game',
      'author': 'james'
  },
  {
      'title': 'megamaze',
      'desc': '3D first-person maze game.',
      'category': 'game',
      'author': 'gardners'
  },
  {
      'title': 'momo',
      'desc': 'A simple game I\'m writing in BASIC for my 2 year old daughter.',
      'category': 'game',
      'author': 'gurce'
  },
  {
      'title': 'dual sid compo',
      'desc': """These are the entries to my October Dual Sid Challenge, in a nice simple wrapper. Proton won the vote for his excellent rendition of X-Files.""",
      'category': 'music',
      'author': 'Shallan50k'
  },
  {
      'title': 'paledit',
      'desc': """simple palette editor

This program lets you edit, load and save the additional sixteen
'highlite'-colours of the vic iii textmode. it is especially useful
for creating tables for colour cycling.

The program theoretically can be expanded for editing the
whole 32 colour palette available in textmode.

The palette data is stored to disk in a sequential file with r,g
and b values for each of the 16 colours.""",
      'category': 'utility',
      'author': 'ubik'
  },
  {
      'title': 'poopie',
      'desc': 'An example of a pure PETSCII game written in BASIC 65, for the MEGA65.',
      'category': 'game',
      'author': 'gurce'
  },
  {
      'title': 'pushem',
      'desc': """A Puzznic clone in 80x25 charset mode for Mega65""",
      'category': 'game',
      'author': 'Endurion'
  },
  {
      'title': 'ramtest',
      'desc': "Bit Shifter's RAM Test program.",
      'category': 'utility',
      'author': 'Bit Shifter'
  },
  {
      'title': 'revolution65',
      'desc': """Strategy game where you attempt to take over a city from the current government by trying to take over the streets and prominent buildings. You can either play against the computer or a human opponent.""",
      'category': 'game',
      'author': 'ubik'
  },
  {
      'title': 'rrb sprites',
      'desc': """I think I've tamed the Raster Rewrite Buffer (RRB) a little by producing a 'soft' sprite routine.
You're seeing 52 NCM sprites, each 16x16 pixels, spinning around using polar coordinates. I've also made use of X and Y flipping.
As you watch, more movement patterns emerge. This version is intended for the Mega65 HW. You can see it in action here :

https://youtu.be/gltOJAuwaX0""",
      'category': 'demo',
      'author': 'geehaf'
  },
  {
      'title': 'ski',
      'desc': """A ski game for the Mega 65 written in Millfork.

Source Code: https://github.com/jaammees/mega-65-ski""",
      'category': 'game',
      'author': 'james'
  },
  {
      'title': 'smashout',
      'desc': 'A (very) simple take on the 1976 Atari classic Breakout',
      'category': 'game',
      'author': 'geehaf'
  },
  {
      'title': 'snow',
      'desc': """Season's Greetings:
A little petscii xmas demo for the MEGA65, using 80x50 characters, extended DMA and lots of snow and wind.""",
      'category': 'demo',
      'author': 'ubik'
  },
  {
      'title': 'testcard',
      'desc': """A test card program, for adjusting the colours of your display and assessing audio output.

Written in BASIC 65.""",
      'category': 'utility',
      'author': 'gurce'
  },
  {
      'title': 'tetris',
      'desc': "Tetris written in BASIC 65.",
      'category': 'game',
      'author': 'zzsila'
  },
  {
      'title': 'vector clock',
      'desc': """This BASIC 65 program shows the current time from RTC using the 640x400 monochrome bitmap mode of the MEGA65.

All characters and digits are drawn as vectors.

During the clock is running, press the Q key for ending it.""",
      'category': 'utility',
      'author': 'Snoopy'
  },
  {
      'title': 'wator',
      'desc': """A population dynamics simulation for the MEGA65.
Sharks and fish wage an ecological war on the toroidal planet Wa-Tor.
For the origins of the wa-tor simulation, see https://en.wikipedia.org/wiki/Wa-Tor""",
      'category': 'demo',
      'author': 'ubik'
  },
  {
      'title': 'wavehero65',
      'desc': """How far can you go on your PWC (personal watercraft), without hitting any rocks or reefs? You start off slowly, but the speed automatically increases as you reach various distance milestones.

This is the MEGA65 version of the C64 game 'Wave Hero' from the 2018 Reset64 4KB Craptastic Game Competition.

This version was written in Millfork, and the src folder in the zip file contains the source code.""",
      'category': 'game',
      'author': 'GeirS'
  },
  {
      'title': 'tutter',
      'desc': """Tutter - Demo of 256 colour FCM, Vertical Char Flips, Raster splits, Palette fades & C64 Music.
The image I've used is a homage to the Tutankhamun images used in early Amiga and Mega 65 demos...

14/11/2021 Appendix : If did this again, I'd use the RRB to smoothly scroll each segment, this version uses raster splits. Cheers, Geehaf.""",
      'category': 'demo',
      'author': 'geehaf'
  },
  {
      'title': 'yaped',
      'desc': """Yaped32: World's first MEGA65 native PETSCII editor supporting 32 colours:
- palette tool for redefining colours and easy creation of gradients
- 9 independent workspaces
- rectangular selection and copy tool
- 5 extra screen rows for help, status info & palettes
- 3 modes of operation: drawing / typing / low-res block
- mouse support (port 1)
Some quick tips:
- Press 'HELP' key in drawing mode for details on how yaped32 works.
- 'RUN/STOP' always takes you back to the main menu
- in drawing mode, press 1-9 to switch between workspaces
- in typing mode, press alt+1-9 to switch between workspaces
- when using the a)rea selection tool in drawing mode, you can switch between workspaces once you have selected an area""",
      'category': 'utility',
      'author': 'ubik'
  }
]

# with open('readfilespublic.php') as json_file:
#     data = json.load(json_file)
#     for item in data:
#         print item['title']
#         print item['fileid']
#         # curl -X POST -d "fileid=d5a875c2-a8c5-4f3e-b196-363f4c9e2bed" https://files.mega65.org/php/readfiledetail.php
#         r = requests.post('https://files.mega65.org/php/readfiledetail.php', data={'fileid': item['fileid']})
#         detail = json.loads(r.text)
#         print detail[0]['description']
#         print '----------------'

def addline(line):
    global lineno, lines
    s = '{} {}\n'.format(lineno, line)
    lineno += 10
    lines.append(s)

def addlabel(lbl):
    global lineno, labels
    labels[lbl] = lineno

labels = {}
lines = []
lineno = 10

# find unique categories
cats = set()
for prg in progs:
    cat = prg['category']
    cat = cat[0].upper() + cat[1:]
    cats.add(cat)

cats = sorted(cats)

_lbl_title = lineno

# Use CHR$(14) to go to lowercase
# Use CHR$(142) to go to uppercase

# buffer current screen contents
addline('rcursor x,y')
addline('rx = x:ry = y')
addline('dma 0, 2000, 2048, 0, 0, 4')
addline('dma 0, 2000, $f800, 1, 2000, 4')

addlabel('.title')
addline('play:palette restore')
addline('if rwindow(2)=40 then print chr$(27)+"x";')
addline('print "{clr}";chr$(142);')
addline('background 0:border 0')
addline('bload "clr.bin",b1,p($f800),r')
addline('bload "screen.bin",b0,p($800),r')

addlabel('.music')
addline('play:envelope 2,0,0,5,0,0')
addline('tempo 25')
addline('rem *** bass line ***')
addline('b1$="o2qd d ia o1 qa ia":b1$=b1$+b1$+b1$+b1$')
addline('b2$="o2qc c ig o1 qg ig":b2$=b2$+b2$')
addline('b3$="o1qg g o2ib o1 qg ig"')
addline('b4$="o1qg o2 ig#fg#fe#f"')
addline('b$="t6"+b1$+b2$+b3$+b4$+"l"')
addline('rem *** gentle arpeggio ***')
addline('a$="t2"')
addline('a1$="o5i#fd#fao6do5a#fa":a1$=a1$+a1$+a1$+a1$')
addline('a2$="o6t2icdco5bo6co5bab"')
addline('a3$="o5abag#fed#f":a3$=a3$+a3$')
addline('a4$="o6co5go6eo5go6go5go6#fp5gp0"')
addline('a$=a$+a1$+a2$+a3$+a4$+"l"')
addline('rem *** main melody ***')
addline('m1$="o5p5t8hergrerdrgrdrcrgr"')
addline('m2$="o5 p5t8h r #f r a r #f r o4 a r o5 #f r c r d r a"')
addline('m1$=m1$+m1$+"p0"')
addline('m2$=m2$+m2$+"p0"')
addline('p1$="o5t9i#f#fq#fi#fq#f#f#fi#fq#fi#f#f":p1$=p1$+p1$')
addline('q1$="o5t9iaaqaiaqaaaiaqaiaa":q1$=q1$+q1$')
addline('p2$="o5t9iggqgigqgggigqgigg":p2$=p2$+p2$')
addline('q2$="o6t9iccqcicqcccicqcicc"')
addline('q3$="o6t9ieeqeieqeeeieqeiee"')
addline('m1$=p1$+p2$+m1$+"l"')
addline('m2$=q1$+q2$+q3$+m2$+"l"')
addline('play b$,a$,m1$,,,m2$:sleep 0.05:play ,,,b$,a$')
addline('cursor 35,17:print "{cyn}demo disk 1"')

# PRETTY LOOP
addline('sc=0:pk=16:s$="press any key to begin!')
addlabel('.tloop')
addline('gosub .drawborder')
addline('x=28:y=20:pk=pk+1:gosub .rainbowstr')
addline('get a$: if a$="" then goto .tloop')
addline('goto .endtitle')

addlabel('.drawborder')
addline('c = sc')
addline('y=0:for x=0 to 78:gosub .drawblock:next x')
addline('x=79:for y=0 to 23:gosub .drawblock:next y')
addline('y=24:for x=79 to 1 step -1:gosub .drawblock:next x')
addline('x=0:for y=24 to 1 step -1:gosub .drawblock:next y')
addline('sc=sc+1:if sc>15 then sc=0')
addline('return')

addlabel('.drawblock')
addline('rem *** draw block ***')
addline('if pk=16 then poke 2048+x+y*80,160')
addline('poke $1f800+x+y*80,64+c')
addline('c=c+1:if c>15 then c=0')
addline('return')

addlabel('.clr')
addline('rem *** clear screen ***')
addline('for y=1 to 23:for x=1 to 78:poke 2048+x+y*80,32:next x:next y')
addline('return')

addlabel('.rainbowstr')
addline('rem *** sub: print rainbow string(x,y,pk,s$) ***')
addline('cursor x,y')
addline('for k=1 to len(s$)')
addline('c$=mid$(s$,k,1)')
addline('foreground mod(k-1+pk,16)+16:print c$;')
addline('next k')
addline('return')

addlabel('.endtitle')
# MAIN MENU
addline('color 1')
addline('palette restore')

addline('bank 128')
addline('gosub .clr')
addline('window 2,2,77,23')

addlabel('.main.')
addline('print "{clr}";chr$(14);')
addline('s$ = "{reverse on}MEGA65 Release Disk{reverse off}"')
addline('print s$')
addline('print')
opt = 1
for cat in cats:
    print(cat)
    addline('print chr$(159);"{}";chr$(5);") {}"'.format(opt, cat))
    opt += 1
addline('print')
addline('print "{cyan}D{white}) Disable auto-boot"')
addline('print "{cyan}X{white}) Exit to BASIC"')
addline('print:print "{cyan}Enter your choice:{white} ";')
addlabel('.mainloop')
addline('get a$')
opt = 1
for cat in cats:
    addline('if a$="{}" then goto .opt_{}.'.format(opt, cat))
    opt += 1

addline('if a$="d" then goto .disable')
addline('if a$="x" then gosub .exitbasic : end')
addline('x=0:y=0:gosub .rainbowstr:pk=pk+1:color 1')
addline('gosub .drawborder')
addline('goto .mainloop')

addlabel('.exitbasic')
addline('play')
# restore prior screen contents
addline('print "{home}{home}{clr}";chr$(142);')
addline('dma 0, 2000, 0, 4, 2048, 0')
addline('dma 0, 2000, 2000, 4, $f800, 1')
addline('cursor rx,ry')
addline('border 6:background 6:color 1')
addline('return')

addlabel('.disable')
addline('print "{clr}";')
addline('s$ = "{reverse on}Disable Auto-boot{reverse off}"')
addline('print s$')
addline('print')
addline('print "- Type \'{cyan}Y{white}\' to disable auto boot into demo disk"')
addline('print "- Any other key will return to main menu"')
addlabel('.dslp.')
addline('get a$')
addline('if a$="y" then begin')
addline('gosub .exitbasic')
addline('q$=chr$(34)+chr$(34)+chr$(20)')
addline('print chr$(17);')
addline('print "rename ";q$;"autoboot.c65";q$;" to ";q$;"menu";q$')
addline('rename "autoboot.c65" to "menu"')
addline('end')
addline('bend')
addline('x=0:y=0:gosub .rainbowstr:pk=pk+1:color 1')
addline('gosub .drawborder')
addline('if a$="" then goto .dslp.')
addline('goto .main.')

# Category menus
for cat in cats:
    addlabel('.opt_{}.'.format(cat))
    addline('print "{clr}";')
    addline('s$ = chr$(18)+"{}"+chr$(146)'.format(cat))
    addline('print s$'.format(cat))
    addline('print')
    opt = 1
    for prg in progs:
        if prg['category'] == cat.lower():
            optval = opt
            if optval > 9:
                optval = chr(ord('A')+optval-10)
            if opt > 9:
                addline('cursor 30, {}'.format(opt-10+2))
            addline('print chr$(159);"{}";chr$(5);") {}"'.format(optval, prg['title'].upper()))
            opt += 1

    if opt > 9:
        addline('cursor 0, 17')
    else:
        addline('print')
    addline('print "{cyan}X{white}) Exit to prior menu"')
    addline('print:print "{cyan}Enter your choice:{white} ";')

    addlabel('.opt_{}_loop'.format(cat))
    addline('get a$')
    opt = 1
    for prg in progs:
        if prg['category'] == cat.lower():
            optval = opt
            if optval > 9:
                optval = chr(ord('a')+optval-10)
            addline('if a$="{}" then goto .prg_{}.'.format(optval, prg['title']))
            opt += 1

    addline('if a$="x" then goto .main.')
    addline('x=0:y=0:gosub .rainbowstr:pk=pk+1:color 1')
    addline('gosub .drawborder')
    addline('goto .opt_{}_loop'.format(cat))

# show program details
for prg in progs:
    addlabel('.prg_{}.'.format(prg['title']))
    cat = prg['category']
    cat = cat[0].upper() + cat[1:]
    addline('print "{clr}";')
    addline('s$ = chr$(18)+"{}"+chr$(146)'.format(prg['title'].upper()))
    addline('print chr$(2);"{}";chr$(130);" : ";s$;" - {}'.format(cat, format(prg['author'])))
    addline('print')
    addline('print "{light gray}";')
    addline('print "{}"'.format('- '*38))
    for ln in prg['desc'].splitlines():
        addline('print "{}"'.format(ln))
    addline('print "{}"'.format('- '*38))
    addline('print "{white}";')
    addline('print')
    addline('print "Press {cyan}X{white} to return to prior menu."');
    addline('print "Press {cyan}RETURN{white} to start program."')
    addlabel('.prg_{}_loop'.format(prg['title']))
    addline('get a$')
    addline('if a$="x" then goto .opt_{}.'.format(cat))
    addline('x={}:y=0:gosub .rainbowstr:pk=pk+1:color 1'.format(len(prg['category'])+3))
    addline('gosub .drawborder')
    addline('if a$<>chr$(13) then goto .prg_{}_loop'.format(prg['title']))
    addline('print "{home}{home}{clr}";chr$(142);:play')
    addline('border 6:background 6:color 1')
    addline('print "loading \'{}\'..."'.format(prg['title']))
    addline('clr:dload "{}"'.format(prg['title']))
    addline('end')


# 2nd pass : replace labels with line numbers
linecnt = 0
for line in lines:
    for label in labels:
        line = line.replace(label, str(labels[label]))
    lines[linecnt] = line
    linecnt += 1

# write lines to file
f = open('autoboot.bas', 'w')
for line in lines:
    f.write(line)
f.close()

