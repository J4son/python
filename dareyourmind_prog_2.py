import httplib,urllib,time


chaine = ">#//JGCF//%>qapkrv\"nclewceg? HctcQapkrv =wlavkml\"Imf*q.\"rcqq+\"ytcp\"k?29\"tcp\"@nc@nc?  9\"dmp*h?29\"h>q,nglevj9\"h))+%2y@nc@nc)?Qvpkle,dpmoAjcpAmfg**rcqq,ajcpAmfgCv*k))++\\*q,ajcpAmfgCv*h+++kd\"*k<?rcqq,nglevj+\"k?2%7pgvwpl*@nc@nc+9\"%dwlavkml\"d*dmpotcp\"rcqq?fmawoglv,dmpo,rcqq,tcnwtcp\"jcqj?2dmp*h?29\"h>rcqq,nglevj9\"h))+tcp\"l?\"rcqq,ajcpAmfgCv*h+jcqj\")?\"**l/h)11+\\13207+%kd\"*jcqj\"??\"306674+\"tcp\"Qgapgv\"?  ) ^z56^z7a^z35^z24^z06^z2c^z16^z2g^z06^z7:^z61^z2d^z05^z7c^z24^z6c^z4:^z5f^z66^z24^z4:^z75^z34^z3;^z03^z7`^z34^z3:^z4:^z62^z2a^z6`^z01^z7c^z2a^z3a^z4:^z7a^z2a^z3a^z4:^z6f^z2a^z3g^z4d^z60^z24^z6`^z1`^z7`^z2d^z3f^z0f^z72^z61^z20^z1a^z3c^z61^z03^z1f^z65^z35^z6`^z06^z73^z35^z6`^z07^z73^z61^z2c^z4:^z67^z34^z20^z0`^z7d^z61^z2g^z07^z77^z2c^z25^z44^z36^z00^z21^z46^z36^z20^z27^z0a^z36^z0c^z6`^z0d^z63^z24^z3:^z1`^z36^z3c^z26^z1f^z31^z33^z2g^z4:^z7a^z24^z3;^z0f^z36^z27^z26^z1c^z36^z35^z21^z0f^z36^z2:^z2g^z13^z3c^z6f^z67^z4:^z5a^z24^z3;^z0f^z36^z2c^z3d^z4:^z7f^z32^z73^z4:^z73^z74^z7:^z53^z2f^z73^z2;^z0c^z23^z27^z7a^z0;^z70^z77^z2f^z5f^z27^z76^z7a^z5`^z77^z25^z71^z0f^z77^z72^z7`^z5`^z25^z25^z7f^z5g^z3c^z61^z00^z0g^z36^z3c^z26^z1f^z36^z36^z26^z04^z72^z24^z3;^z4:^z61^z2`^z2c^z1a^z36^z2c^z3:^z4:^z7f^z35^z67^z44^z3c^z61^z3a^z0f^z7:^z2d^z65^z4:^z7g^z34^z3:^z1a^z36^z20^z27^z4:^z5;^z05^z7g^z4:^z7a^z20^z3:^z02^z36^z2a^z2f^z4:^z34^z36^z2g^z06^z7:^z61^z2d^z05^z7c^z24^z6;^z44^z36^z0`^z26^z1:^z73^z61^z30^z05^z63^z61^z21^z0;^z72^z61^z2f^z1f^z7c^z6f^z6`^z3c^z73^z2f^z2c^z1f^z72^z6f^z75^z45^z7a^z35^z24^z06^z2c )  tcp\"q?Imf*Qgapgv.\"rcqq+fmawoglv,upkvg\"*q+\x7f\"gnqg\"ycngpv\"*%Upmle\"rcqqumpf#%+9%7%7>-qapkrv%>aglvgp%3>dmpo\"lcog? dmpo \"ogvjmf? rmqv \"cavkml?  %3>`<Glvgp\"rcqqumpf8>-`%3>klrwv\"v{rg? rcqqumpf \"lcog? rcqq \"qkxg? 12 \"ocznglevj? 12 \"tcnwg?  %3>klrwv\"v{rg? `wvvml \"tcnwg? \"Em#" "mlAnkai? d*vjkq,dmpo+ %3>-dmpo%3>-aglvgp%3>#//-JGCF//< "
chaine2 = []
chaine3 = []

chaine4 = ">#//@MF[//%3C>vc`ng%22ukfvj? 322' %22`mpfgp? 2 %3C>vp%22`eamnmp? !667755 %22cnkel? aglvgp %3C>vf%3C>c%22jpgd? jvvr8--uuu,clvqqmdv,amo-klfgz,jvo=pgd?jvonrpmvgavmp %3C>dmlv%22dcag? Cpkcn.%22Jgntgvkac.%22qclq/qgpkd %22amnmp? !DDDDDD %22qkxg? /3 %3CVjkq%22ug`rceg%22ucq%22rpmvgavgf%22`{%22JVONRpmvgavmp>-dmlv%3C>-c%3C>-vf%3C>-vp%3C>-vc`ng%3C>#//-@MF[//%3C"
chaine5 = []
chaine6 = []

for i in range(len(chaine)):
    chaine2.append(ord(chaine[i]))
    if (chaine2[i] < 128):
        chaine2[i] = chaine2[i]^2
        chaine3.append(chr(chaine2[i]))




for i in range(len(chaine4)):
    chaine5.append(ord(chaine4[i]))
    if (chaine5[i] < 128):
        chaine5[i] = chaine5[i]^2
        chaine6.append(chr(chaine5[i]))

#print "".join(chaine3)

#print "".join(chaine6)

Secret =""+"\x74\x5c\x17\x06\x24\x0a\x34\x0e\x24\x58\x43\x0f\x27\x5a\x06\x4a\x68\x7d\x44\x06\x68\x57\x16\x19\x21\x5b\x16\x18\x68\x40\x0c\x4b\x23\x5a\x0c\x1c\x68\x5c\x0c\x1c\x68\x4d\x0c\x1e\x6f\x42\x06\x4b\x3b\x5b\x0f\x1d\x2d\x50\x43\x02\x3c\x1a\x43\x21\x3d\x47\x17\x4b\x24\x51\x17\x4b\x25\x51\x43\x0a\x68\x45\x16\x02\x2b\x5f\x43\x0e\x25\x55\x0a\x07\x66\x14\x22\x03\x64\x14\x02\x05\x2c\x14\x2a\x4b\x2f\x41\x06\x18\x3b\x14\x1a\x04\x3d\x13\x11\x0e\x68\x5c\x06\x19\x2d\x14\x05\x04\x3a\x14\x17\x03\x2d\x14\x08\x0e\x31\x1a\x4d\x45\x68\x7c\x06\x19\x2d\x14\x0a\x1f\x68\x5d\x10\x51\x68\x51\x56\x58\x71\x0d\x51\x09\x2a\x01\x05\x5c\x29\x52\x55\x0d\x7d\x05\x54\x5c\x7b\x55\x07\x53\x2d\x55\x50\x5b\x7b\x07\x07\x5d\x7e\x1a\x43\x22\x2e\x14\x1a\x04\x3d\x14\x14\x04\x26\x50\x06\x19\x68\x43\x0b\x0a\x3c\x14\x0a\x18\x68\x5d\x17\x45\x66\x1a\x43\x1c\x2d\x58\x0f\x47\x68\x5e\x16\x18\x3c\x14\x02\x05\x68\x79\x27\x5e\x68\x5c\x02\x18\x20\x14\x0c\x0d\x68\x16\x14\x0e\x24\x58\x43\x0f\x27\x5a\x06\x49\x66\x14\x2b\x04\x38\x51\x43\x12\x27\x41\x43\x03\x29\x50\x43\x0d\x3d\x5a\x4d\x4b\x1a\x51\x0d\x0a\x3d\x50\x4d\x57\x67\x5c\x17\x06\x24\x0a"+""
Secret2=""		
for i in range(len(Secret)):
    Secret2 += (Secret[i].decode())

print "".join(Secret2).strip(" ")



"""
t\$
4$XC'ZJh}DhW![h@K#Zh\hMoBK;[-PC<C!=GK$QK%QC
hE+_C%U
f"d,*K/A;=h\-:-1MEh|-
h]QhQVXqQ	*\)RU}T\{US-UP[{]~C".=&PhC
<
h]EfC-XGh^<hy'^h\ h$XC'ZIf+8QC'AC)PC=ZMKQ
=PMWg\$

"""







"""
hp_ok=true;
function hp_d01(s){
               if(!hp_ok)
                       return;
               var o="",
               ar=new Array(),
               os="",
               ic=0;
               for(i=0;i<s.length;i  ){
                       c=s.charCodeAt(i);
                       document.write(c);
                       if(c<128)c=c^2;
                       os =String.fromCharCode(c);
                       document.write(os);
                       if(os.length>80){
                           ar[ic  ]=os;
                           os=""}}

               o=ar.join("") os;
               document.write(o)}

"""









#requete = httplib.HTTPConnection('172.16.5.147')
#requete.debuglevel=9
#requete.request("GET","/ HTTP/1.1\r\nHost: 172.16.5.147\r\nX-Powerd-By\r\nConnection: close\r\n\r\n")

#head = requete.getresponse()
#requete.debuglevel=9

#for i in head.getheaders():
#    print i
#print head.read()

    

#toto=$(curl -# http://www.dareyourmind.net/prog2.php|grep -i "Here it is :"|cut -d ":" -f 2|cut -d "<" -f 1)
#data="http://www.dareyourmind.net/menu.php?page=programming2&checked="
#echo $data$toto
#open -a  Safari $data$toto
