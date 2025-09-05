# ---------------- IMPORTS ---------------- #
import string, webbrowser, numpy as np
import os, math, sys
BASE_DIR = os.path.dirname(__file__)
# When frozen by PyInstaller, use the extraction directory for bundled data
try:
    _frozen_base = getattr(sys, "_MEIPASS", None)
    if _frozen_base:
        BASE_DIR = _frozen_base
except Exception:
    pass
from tkinter import BOTH, END, LEFT, NORMAL, DISABLED, simpledialog, BOTTOM, X, PhotoImage, Canvas
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
# Pillow 10+ removed Image.ANTIALIAS; use a compatible resampling fallback
try:
    RESAMPLE = Image.Resampling.LANCZOS  # Pillow >= 10
except Exception:
    RESAMPLE = getattr(Image, 'LANCZOS', getattr(Image, 'BICUBIC', 1))

# ---------------- CIPHERS ---------------- #

# Load large English word list for Caesar bruteforce from an embedded file (bundled via PyInstaller) with fallback

def load_english_words():
    words = set()
    path = os.path.join(BASE_DIR, "assets", "words.txt")
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith('#'):
                    continue
                for w in s.replace(",", " ").replace(";", " ").split():
                    w = w.strip().lower()
                    if w:
                        words.add(w)
    except Exception:
        # Fallback minimal list if words.txt is not bundled
        fallback = (
            "the be to of and a in that have i it for not on with he as you do at this "
            "but his by from they we say her she or an will my one all would there their "
            "what so up out if about who get which go me when make can like time no just him "
            "know take people into year your good some could them see other than then now look "
            "only come its over think also back after use two how our work first well way even new "
            "want because any these give day most us"
        )
        words.update(fallback.split())
    return words

ENGLISH_WORDS = set("""the of and to a in for is on that by this with i you it not or be are from at as your all have new more an was we will home can us about if page my has search free but our one other do no information time they site he up may what which their news out use any there see only so his when contact here business who web also now help get pm view online c e first am been would how were me s services some these click its like service x than find price date back top people had list name just over state year day into email two health n world re next used go b work last most products music buy data make them should product system post her city t add policy number such please available copyright support message after best software then jan good video well d where info rights public books high school through m each links she review years order very privacy book items company r read group sex need many user said de does set under general research university january mail full map reviews program life know games way days management p part could great united hotel real f item international center ebay must store travel comments made development report off member details line terms before hotels did send right type because local those using results office education national car design take posted internet address community within states area want phone dvd shipping reserved subject between forum family l long based w code show o even black check special prices website index being women much sign file link open today technology south case project same pages uk version section own found sports house related security both g county american photo game members power while care network down computer systems three total place end following download h him without per access think north resources current posts big media law control water history pictures size art personal since including guide shop directory board location change white text small rating rate government children during usa return students v shopping account times sites level digital profile previous form events love old john main call hours image department title description non k y insurance another why shall property class cd still money quality every listing content country private little visit save tools low reply customer december compare movies include college value article york man card jobs provide j food source author different press u learn sale around print course job canada process teen room stock training too credit point join science men categories advanced west sales look english left team estate box conditions select windows photos gay thread week category note live large gallery table register however june october november market library really action start series model features air industry plan human provided tv yes required second hot accessories cost movie forums march la september better say questions july yahoo going medical test friend come dec server pc study application cart staff articles san feedback again play looking issues april never users complete street topic comment financial things working against standard tax person below mobile less got blog party payment equipment login student let programs offers legal above recent park stores side act problem red give memory performance social q august quote language story sell options experience rates create key body young america important field few east paper single ii age activities club example girls additional password z latest something road gift question changes night ca hard texas oct pay four poker status browse issue range building seller court february always result audio light write war nov offer blue groups al easy given files event release analysis request fax china making picture needs possible might professional yet month major star areas future space committee hand sun cards problems london washington meeting rss become interest id child keep enter california porn share similar garden schools million added reference companies listed baby learning energy run delivery net popular term film stories put computers journal reports co try welcome central images president notice god original head radio until cell color self council away includes track australia discussion archive once others entertainment agreement format least society months log safety friends sure faq trade edition cars messages marketing tell further updated association able having provides david fun already green studies close common drive specific several gold feb living sep collection called short arts lot ask display limited powered solutions means director daily beach past natural whether due et electronics five upon period planning database says official weather mar land average done technical window france pro region island record direct microsoft conference environment records st district calendar costs style url front statement update parts aug ever downloads early miles sound resource present applications either ago document word works material bill apr written talk federal hosting rules final adult tickets thing centre requirements via cheap nude kids finance true minutes else mark third rock gifts europe reading topics bad individual tips plus auto cover usually edit together videos percent fast function fact unit getting global tech meet far economic en player projects lyrics often subscribe submit germany amount watch included feel though bank risk thanks everything deals various words linux jul production commercial james weight town heart advertising received choose treatment newsletter archives points knowledge magazine error camera jun girl currently construction toys registered clear golf receive domain methods chapter makes protection policies loan wide beauty manager india position taken sort listings models michael known half cases step engineering florida simple quick none wireless license paul friday lake whole annual published later basic sony shows corporate google church method purchase customers active response practice hardware figure materials fire holiday chat enough designed along among death writing speed html countries loss face brand discount higher effects created remember standards oil bit yellow political increase advertise kingdom base near environmental thought stuff french storage oh japan doing loans shoes entry stay nature orders availability africa summary turn mean growth notes agency king monday european activity copy although drug pics western income force cash employment overall bay river commission ad package contents seen players engine port album regional stop supplies started administration bar institute views plans double dog build screen exchange types soon sponsored lines electronic continue across benefits needed season apply someone held ny anything printer condition effective believe organization effect asked eur mind sunday selection casino pdf lost tour menu volume cross anyone mortgage hope silver corporation wish inside solution mature role rather weeks addition came supply nothing certain usr executive running lower necessary union jewelry according dc clothing mon com particular fine names robert homepage hour gas skills six bush islands advice career military rental decision leave british teens pre huge sat woman facilities zip bid kind sellers middle move cable opportunities taking values division coming tuesday object lesbian appropriate machine logo length actually nice score statistics client ok returns capital follow sample investment sent shown saturday christmas england culture band flash ms lead george choice went starting registration fri thursday courses consumer hi airport foreign artist outside furniture levels channel letter mode phones ideas wednesday structure fund summer allow degree contract button releases wed homes super male matter custom virginia almost took located multiple asian distribution editor inn industrial cause potential song cnet ltd los hp focus late fall featured idea rooms female responsible inc communications win associated thomas primary cancer numbers reason tool browser spring foundation answer voice eg friendly schedule documents communication purpose feature bed comes police everyone independent ip approach cameras brown physical operating hill maps medicine deal hold ratings chicago forms glass happy tue smith wanted developed thank safe unique survey prior telephone sport ready feed animal sources mexico population pa regular secure navigation operations therefore ass simply evidence station christian round paypal favorite understand option master valley recently probably thu rentals sea built publications blood cut worldwide improve connection publisher hall larger anti networks earth parents nokia impact transfer introduction kitchen strong tel carolina wedding properties hospital ground overview ship accommodation owners disease tx excellent paid italy perfect hair opportunity kit classic basis command cities william express anal award distance tree peter assessment ensure thus wall ie involved el extra especially interface pussy partners budget rated guides success maximum ma operation existing quite selected boy amazon patients restaurants beautiful warning wine locations horse vote forward flowers stars significant lists technologies owner retail animals useful directly manufacturer ways est son providing rule mac housing takes iii gmt bring catalog searches max trying mother authority considered told xml traffic programme joined input strategy feet agent valid bin modern senior ireland sexy teaching door grand testing trial charge units instead canadian cool normal wrote enterprise ships entire educational md leading metal positive fl fitness chinese opinion mb asia football abstract uses output funds mr greater likely develop employees artists alternative processing responsibility resolution java guest seems publication pass relations trust van contains session multi photography republic fees components vacation century academic assistance completed skin graphics indian prev ads mary il expected ring grade dating pacific mountain organizations pop filter mailing vehicle longer consider int northern behind panel floor german buying match proposed default require iraq boys outdoor deep morning otherwise allows rest protein plant reported hit transportation mm pool mini politics partner disclaimer authors boards faculty parties fish membership mission eye string sense modified pack released stage internal goods recommended born unless richard detailed japanese race approved background target except character usb maintenance ability maybe functions ed moving brands places php pretty trademarks phentermine spain southern yourself etc winter rape battery youth pressure submitted boston incest debt keywords medium television interested core break purposes throughout sets dance wood msn itself defined papers playing awards fee studio reader virtual device established answers rent las remote dark programming external apple le regarding instructions min offered theory enjoy remove aid surface minimum visual host variety teachers isbn martin manual block subjects agents increased repair fair civil steel understanding songs fixed wrong beginning hands associates finally az updates desktop classes paris ohio gets sector capacity requires jersey un fat fully father electric saw instruments quotes officer driver businesses dead respect unknown specified restaurant mike trip pst worth mi procedures poor teacher xxx eyes relationship workers farm fucking georgia peace traditional campus tom showing creative coast benefit progress funding devices lord grant sub agree fiction hear sometimes watches careers beyond goes families led museum themselves fan transport interesting blogs wife evaluation accepted former implementation ten hits zone complex th cat galleries references die presented jack flat flow agencies literature respective parent spanish michigan columbia setting dr scale stand economy highest helpful monthly critical frame musical definition secretary angeles networking path australian employee chief gives kb bottom magazines packages detail francisco laws changed pet heard begin individuals colorado royal clean switch russian largest african guy titles relevant guidelines justice connect bible dev cup basket applied weekly vol installation described demand pp suite vegas na square chris attention advance skip diet army auction gear lee os difference allowed correct charles nation selling lots piece sheet firm seven older illinois regulations elements species jump cells module resort facility random pricing dvds certificate minister motion looks fashion directions visitors documentation monitor trading forest calls whose coverage couple giving chance vision ball ending clients actions listen discuss accept automotive naked goal successful sold wind communities clinical situation sciences markets lowest highly publishing appear emergency developing lives currency leather determine milf temperature palm announcements patient actual historical stone bob commerce ringtones perhaps persons difficult scientific satellite fit tests village accounts amateur ex met pain xbox particularly factors coffee www settings cum buyer cultural steve easily oral ford poster edge functional root au fi closed holidays ice pink zealand balance monitoring graduate replies shot nc architecture initial label thinking scott llc sec recommend canon hardcore league waste minute bus provider optional dictionary cold accounting manufacturing sections chair fishing effort phase fields bag fantasy po letters motor va professor context install shirt apparel generally continued foot mass crime count breast techniques ibm rd johnson sc quickly dollars websites religion claim driving permission surgery patch heat wild measures generation kansas miss chemical doctor task reduce brought himself nor component enable exercise bug santa mid guarantee leader diamond israel se processes soft servers alone meetings seconds jones arizona keyword interests flight congress fuel username walk fuck produced italian paperback classifieds wait supported pocket saint rose freedom argument competition creating jim drugs joint premium providers fresh characters attorney upgrade di factor growing thousands km stream apartments pick hearing eastern auctions therapy entries dates generated signed upper administrative serious prime samsung limit began louis steps errors shops bondage del efforts informed ga ac thoughts creek ft worked quantity urban practices sorted reporting essential myself tours platform load affiliate labor immediately admin nursing defense machines designated tags heavy covered recovery joe guys integrated configuration cock merchant comprehensive expert universal protect drop solid cds presentation languages became orange compliance vehicles prevent theme rich im campaign marine improvement vs guitar finding pennsylvania examples ipod saying spirit ar claims porno challenge motorola acceptance strategies mo seem affairs touch intended towards sa goals hire election suggest branch charges serve affiliates reasons magic mount smart talking gave ones latin multimedia xp tits avoid certified manage corner rank computing oregon element birth virus abuse interactive requests separate quarter procedure leadership tables define racing religious facts breakfast kong column plants faith chain developer identify avenue missing died approximately domestic sitemap recommendations moved houston reach comparison mental viewed moment extended sequence inch attack sorry centers opening damage lab reserve recipes cvs gamma plastic produce snow placed truth counter failure follows eu weekend dollar camp ontario automatically des minnesota films bridge native fill williams movement printing baseball owned approval draft chart played contacts cc jesus readers clubs lcd wa jackson equal adventure matching offering shirts profit leaders posters institutions assistant variable ave dj advertisement expect parking headlines yesterday compared determined wholesale workshop russia gone codes kinds extension seattle statements golden completely teams fort cm wi lighting senate forces funny brother gene turned portable tried electrical applicable disc returned pattern ct hentai boat named theatre laser earlier manufacturers sponsor classical icon warranty dedicated indiana direction harry basketball objects ends delete evening assembly nuclear taxes mouse signal criminal issued brain sexual wisconsin powerful dream obtained false da cast flower felt personnel passed supplied identified falls pic soul aids opinions promote stated stats hawaii professionals appears carry flag decided nj covers hr em advantage hello designs maintain tourism priority newsletters adults clips savings iv graphic atom payments rw estimated binding brief ended winning eight anonymous iron straight script served wants miscellaneous prepared void dining alert integration atlanta dakota tag interview mix framework disk installed queen vhs credits clearly fix handle sweet desk criteria pubmed dave massachusetts diego hong vice associate ne truck behavior enlarge ray frequently revenue measure changing votes du duty looked discussions bear gain festival laboratory ocean flights experts signs lack depth iowa whatever logged laptop vintage train exactly dry explore maryland spa concept nearly eligible checkout reality forgot handling origin knew gaming feeds billion destination scotland faster intelligence dallas bought con ups nations route followed specifications broken tripadvisor frank alaska zoom blow battle residential anime speak decisions industries protocol query clip partnership editorial nt expression es equity provisions speech wire principles suggestions rural shared sounds replacement tape strategic judge spam economics acid bytes cent forced compatible fight apartment height null zero speaker filed gb netherlands obtain bc consulting recreation offices designer remain managed pr failed marriage roll korea banks fr participants secret bath aa kelly leads negative austin favorites toronto theater springs missouri andrew var perform healthy translation estimates font assets injury mt joseph ministry drivers lawyer figures married protected proposal sharing philadelphia portal waiting birthday beta fail gratis banking officials brian toward won slightly assist conduct contained lingerie shemale legislation calling parameters jazz serving bags profiles miami comics matters houses doc postal relationships tennessee wear controls breaking combined ultimate wales representative frequency introduced minor finish departments residents noted displayed mom reduced physics rare spent performed extreme samples davis daniel bars reviewed row oz forecast removed helps singles administrator cycle amounts contain accuracy dual rise usd sleep mg bird pharmacy brazil creation static scene hunter addresses lady crystal famous writer chairman violence fans oklahoma speakers drink academy dynamic gender eat permanent agriculture dell cleaning constitutes portfolio practical delivered collectibles infrastructure exclusive seat concerns colour vendor originally intel utilities philosophy regulation officers reduction aim bids referred supports nutrition recording regions junior toll les cape ann rings meaning tip secondary wonderful mine ladies henry ticket announced guess agreed prevention whom ski soccer math import posting presence instant mentioned automatic healthcare viewing maintained ch increasing majority connected christ dan dogs sd directors aspects austria ahead moon participation scheme utility preview fly manner matrix containing combination devel amendment despite strength guaranteed turkey libraries proper distributed degrees singapore enterprises delta fear seeking inches phoenix rs convention shares principal daughter standing voyeur comfort colors wars cisco ordering kept alpha appeal cruise bonus certification previously hey bookmark buildings specials beat disney household batteries adobe smoking bbc becomes drives arms alabama tea improved trees avg achieve positions dress subscription dealer contemporary sky utah nearby rom carried happen exposure panasonic hide permalink signature gambling refer miller provision outdoors clothes caused luxury babes frames viagra certainly indeed newspaper toy circuit layer printed slow removal easier src liability trademark hip printers faqs nine adding kentucky mostly eric spot taylor trackback prints spend factory interior revised grow americans optical promotion relative amazing clock dot hiv identity suites conversion feeling hidden reasonable victoria serial relief revision broadband influence ratio pda importance rain onto dsl planet webmaster copies recipe zum permit seeing proof dna diff tennis bass prescription bedroom empty instance hole pets ride licensed orlando specifically tim bureau maine sql represent conservation pair ideal specs recorded don pieces finished parks dinner lawyers sydney stress cream ss runs trends yeah discover sexo ap patterns boxes louisiana hills javascript fourth nm advisor mn marketplace nd evil aware wilson shape evolution irish certificates objectives stations suggested gps op remains acc greatest firms concerned euro operator structures generic encyclopedia usage cap ink charts continuing mixed census interracial peak tn competitive exist wheel transit dick suppliers salt compact poetry lights tracking angel bell keeping preparation attempt receiving matches accordance width noise engines forget array discussed accurate stephen elizabeth climate reservations pin playstation alcohol greek instruction managing annotation sister raw differences walking explain smaller newest establish gnu happened expressed jeff extent sharp lesbians ben lane paragraph kill mathematics aol compensation ce export managers aircraft modules sweden conflict conducted versions employer occur percentage knows mississippi describe concern backup requested citizens connecticut heritage personals immediate holding trouble spread coach kevin agricultural expand supporting audience assigned jordan collections ages participate plug specialist cook affect virgin experienced investigation raised hat institution directed dealers searching sporting helping perl affected lib bike totally plate expenses indicate blonde ab proceedings favourite transmission anderson utc characteristics der lose organic seek experiences albums cheats extremely verzeichnis contracts guests hosted diseases concerning developers equivalent chemistry tony neighborhood nevada kits thailand variables agenda anyway continues tracks advisory cam curriculum logic template prince circle soil grants anywhere psychology responses atlantic wet circumstances edward investor identification ram leaving wildlife appliances matt elementary cooking speaking sponsors fox unlimited respond sizes plain exit entered iran arm keys launch wave checking costa belgium printable holy acts guidance mesh trail enforcement symbol crafts highway buddy hardcover observed dean setup poll booking glossary fiscal celebrity styles denver unix filled bond channels ericsson appendix notify blues chocolate pub portion scope hampshire supplier cables cotton bluetooth controlled requirement authorities biology dental killed border ancient debate representatives starts pregnancy causes arkansas biography leisure attractions learned transactions notebook explorer historic attached opened tm husband disabled authorized crazy upcoming britain concert retirement scores financing efficiency sp comedy adopted efficient weblog linear commitment specialty bears jean hop carrier edited constant visa mouth jewish meter linked portland interviews concepts nh gun reflect pure deliver wonder hell lessons fruit begins qualified reform lens alerts treated discovery draw mysql classified relating assume confidence alliance fm confirm warm neither lewis howard offline leaves engineer lifestyle consistent replace clearance connections inventory converter suck organisation babe checks reached becoming blowjob safari objective indicated sugar crew legs sam stick securities allen pdt relation enabled genre slide montana volunteer tested rear democratic enhance switzerland exact bound parameter adapter processor node formal dimensions contribute lock hockey storm micro colleges laptops mile showed challenges editors mens threads bowl supreme brothers recognition presents ref tank submission dolls estimate encourage navy kid regulatory inspection consumers cancel limits territory transaction manchester weapons paint delay pilot outlet contributions continuous db czech resulting cambridge initiative novel pan execution disability increases ultra winner idaho contractor ph episode examination potter dish plays bulletin ia pt indicates modify oxford adam truly epinions painting committed extensive affordable universe candidate databases patent slot psp outstanding ha eating perspective planned watching lodge messenger mirror tournament consideration ds discounts sterling sessions kernel boobs stocks buyers journals gray catalogue ea jennifer antonio charged broad taiwan und chosen demo greece lg swiss sarah clark labour hate terminal publishers nights behalf caribbean liquid rice nebraska loop salary reservation foods gourmet guard properly orleans saving nfl remaining empire resume twenty newly raise prepare avatar gary depending illegal expansion vary hundreds rome arab lincoln helped premier tomorrow purchased milk decide consent drama visiting performing downtown keyboard contest collected nw bands boot suitable ff absolutely millions lunch dildo audit push chamber guinea findings muscle featuring iso implement clicking scheduled polls typical tower yours sum misc calculator significantly chicken temporary attend shower alan sending jason tonight dear sufficient holdem shell province catholic oak vat awareness vancouver governor beer seemed contribution measurement swimming spyware formula constitution packaging solar jose catch jane pakistan ps reliable consultation northwest sir doubt earn finder unable periods classroom tasks democracy attacks kim wallpaper merchandise const resistance doors symptoms resorts biggest memorial visitor twin forth insert baltimore gateway ky dont alumni drawing candidates charlotte ordered biological fighting transition happens preferences spy romance instrument bruce split themes powers heaven br bits pregnant twice classification focused egypt physician hollywood bargain wikipedia cellular norway vermont asking blocks normally lo spiritual hunting diabetes suit ml shift chip res sit bodies photographs cutting wow simon writers marks flexible loved favourites mapping numerous relatively birds satisfaction represents char indexed pittsburgh superior preferred saved paying cartoon shots intellectual moore granted choices carbon spending comfortable magnetic interaction listening effectively registry crisis outlook massive denmark employed bright treat header cs poverty formed piano echo que grid sheets patrick experimental puerto revolution consolidation displays plasma allowing earnings voip mystery landscape dependent mechanical journey delaware bidding consultants risks banner applicant charter fig barbara cooperation counties acquisition ports implemented sf directories recognized dreams blogger notification kg licensing stands teach occurred textbooks rapid pull hairy diversity cleveland ut reverse deposit seminar investments latina nasa wheels sexcam specify accessibility dutch sensitive templates formats tab depends boots holds router concrete si editing poland folder womens css completion upload pulse universities technique contractors milfhunter voting courts notices subscriptions calculate mc detroit alexander broadcast converted metro toshiba anniversary improvements strip specification pearl accident nick accessible accessory resident plot qty possibly airline typically representation regard pump exists arrangements smooth conferences uniprotkb beastiality strike consumption birmingham flashing lp narrow afternoon threat surveys sitting putting consultant controller ownership committees penis legislative researchers vietnam trailer anne castle gardens missed malaysia unsubscribe antique labels willing bio molecular upskirt acting heads stored exam logos residence attorneys milfs antiques density hundred ryan operators strange sustainable philippines statistical beds breasts mention innovation pcs employers grey parallel honda amended operate bills bold bathroom stable opera definitions von doctors lesson cinema asset ag scan elections drinking blowjobs reaction blank enhanced entitled severe generate stainless newspapers hospitals vi deluxe humor aged monitors exception lived duration bulk successfully indonesia pursuant sci fabric edt visits primarily tight domains capabilities pmid contrast recommendation flying recruitment sin berlin cute organized ba para siemens adoption improving cr expensive meant capture pounds buffalo organisations plane pg explained seed programmes desire expertise mechanism camping ee jewellery meets welfare peer caught eventually marked driven measured medline bottle agreements considering innovative marshall massage rubber conclusion closing tampa thousand meat legend grace susan ing ks adams python monster alex bang villa bone columns disorders bugs collaboration hamilton detection ftp cookies inner formation tutorial med engineers entity cruises gate holder proposals moderator sw tutorials settlement portugal lawrence roman duties valuable erotic tone collectables ethics forever dragon busy captain fantastic imagine brings heating leg neck hd wing governments purchasing scripts abc stereo appointed taste dealing commit tiny operational rail airlines liberal livecam jay trips gap sides tube turns corresponding descriptions cache belt jacket determination animation oracle er matthew lease productions aviation hobbies proud excess disaster console commands jr telecommunications instructor giant achieved injuries shipped bestiality seats approaches biz alarm voltage anthony nintendo usual loading stamps appeared franklin angle rob vinyl highlights mining designers melbourne ongoing worst imaging betting scientists liberty wyoming blackjack argentina era convert possibility analyst commissioner dangerous garage exciting reliability thongs gcc unfortunately respectively volunteers attachment ringtone finland morgan derived pleasure honor asp oriented eagle desktops pants columbus nurse prayer appointment workshops hurricane quiet luck postage producer represented mortgages dial responsibilities cheese comic carefully jet productivity investors crown par underground diagnosis maker crack principle picks vacations gang semester calculated cumshot fetish applies casinos appearance smoke apache filters incorporated nv craft cake notebooks apart fellow blind lounge mad algorithm semi coins andy gross strongly cafe valentine hilton ken proteins horror su exp familiar capable douglas debian till involving pen investing christopher admission epson shoe elected carrying victory sand madison terrorism joy editions cpu mainly ethnic ran parliament actor finds seal situations fifth allocated citizen vertical corrections structural municipal describes prize sr occurs jon absolute disabilities consists anytime substance prohibited addressed lies pipe soldiers nr guardian lecture simulation layout initiatives ill concentration classics lbs lay interpretation horses lol dirty deck wayne donate taught bankruptcy mp worker optimization alive temple substances prove discovered wings breaks genetic restrictions participating waters promise thin exhibition prefer ridge cabinet modem harris mph bringing sick dose evaluate tiffany tropical collect bet composition toyota streets nationwide vector definitely shaved turning buffer purple existence commentary larry limousines developments def immigration destinations lets mutual pipeline necessarily syntax li attribute prison skill chairs nl everyday apparently surrounding mountains moves popularity inquiry ethernet checked exhibit throw trend sierra visible cats desert postposted ya oldest rhode nba busty coordinator obviously mercury steven handbook greg navigate worse summit victims epa spaces fundamental burning escape coupons somewhat receiver substantial tr progressive cialis bb boats glance scottish championship arcade richmond sacramento impossible ron russell tells obvious fiber depression graph covering platinum judgment bedrooms talks filing foster modeling passing awarded testimonials trials tissue nz memorabilia clinton masters bonds cartridge alberta explanation folk org commons cincinnati subsection fraud electricity permitted spectrum arrival okay pottery emphasis roger aspect workplace awesome mexican confirmed counts priced wallpapers hist crash lift desired inter closer assumes heights shadow riding infection firefox lisa expense grove eligibility venture clinic korean healing princess mall entering packet spray studios involvement dad buttons placement observations vbulletin funded thompson winners extend roads subsequent pat dublin rolling fell motorcycle yard disclosure establishment memories nelson te arrived creates faces tourist cocks av mayor murder sean adequate senator yield presentations grades cartoons pour digest reg lodging tion dust hence wiki entirely replaced radar rescue undergraduate losses combat reducing stopped occupation lakes butt donations associations citysearch closely radiation diary seriously kings shooting kent adds nsw ear flags pci baker launched elsewhere pollution conservative guestbook shock effectiveness walls abroad ebony tie ward drawn arthur ian visited roof walker demonstrate atmosphere suggests kiss beast ra operated experiment targets overseas purchases dodge counsel federation pizza invited yards assignment chemicals gordon mod farmers rc queries bmw rush ukraine absence nearest cluster vendors mpeg whereas yoga serves woods surprise lamp rico partial shoppers phil everybody couples nashville ranking jokes cst http ceo simpson twiki sublime counseling palace acceptable satisfied glad wins measurements verify globe trusted copper milwaukee rack medication warehouse shareware ec rep dicke kerry receipt supposed ordinary nobody ghost violation configure stability mit applying southwest boss pride institutional expectations independence knowing reporter metabolism keith champion cloudy linda ross personally chile anna plenty solo sentence throat ignore maria uniform excellence wealth tall rm somewhere vacuum dancing attributes recognize brass writes plaza pdas outcomes survival quest publish sri screening toe thumbnail trans jonathan whenever nova lifetime api pioneer booty forgotten acrobat plates acres venue athletic thermal essays behaviour vital telling fairly coastal config cf charity intelligent edinburgh vt excel modes obligation campbell wake stupid harbor hungary traveler urw segment realize regardless lan enemy puzzle rising aluminum wells wishlist opens insight sms shit restricted republican secrets lucky latter merchants thick trailers repeat syndrome philips attendance penalty drum glasses enables nec iraqi builder vista jessica chips terry flood foto ease arguments amsterdam orgy arena adventures pupils stewart announcement tabs outcome xx appreciate expanded casual grown polish lovely extras gm centres jerry clause smile lands ri troops indoor bulgaria armed broker charger regularly believed pine cooling tend gulf rt rick trucks cp mechanisms divorce laura shopper tokyo partly nikon customize tradition candy pills tiger donald folks sensor exposed telecom hunt angels deputy indicators sealed thai emissions physicians loaded fred complaint scenes experiments balls afghanistan dd boost spanking scholarship governance mill founded supplements chronic icons tranny moral den catering aud finger keeps pound locate camcorder pl trained burn implementing roses labs ourselves bread tobacco wooden motors tough roberts incident gonna dynamics lie crm rf conversation decrease cumshots chest pension billy revenues emerging worship bukkake capability ak fe craig herself producing churches precision damages reserves contributed solve shorts reproduction minority td diverse amp ingredients sb ah johnny sole franchise recorder complaints facing sm nancy promotions tones passion rehabilitation maintaining sight laid clay defence patches weak refund usc towns environments trembl divided blvd reception amd wise emails cyprus wv odds correctly insider seminars consequences makers hearts geography appearing integrity worry ns discrimination eve carter legacy marc pleased danger vitamin widely processed phrase genuine raising implications functionality paradise hybrid reads roles intermediate emotional sons leaf pad glory platforms ja bigger billing diesel versus combine overnight geographic exceed bs rod saudi fault cuba hrs preliminary districts introduce silk promotional kate chevrolet babies bi karen compiled romantic revealed specialists generator albert examine jimmy graham suspension bristol margaret compaq sad correction wolf slowly authentication communicate rugby supplement showtimes cal portions infant promoting sectors samuel fluid grounds fits kick regards meal ta hurt machinery bandwidth unlike equation baskets probability pot dimension wright img barry proven schedules admissions cached warren slip studied reviewer involves quarterly rpm profits devil grass comply marie florist illustrated cherry continental alternate deutsch achievement limitations kenya webcam cuts funeral nutten earrings enjoyed automated chapters pee charlie quebec nipples passenger convenient dennis mars francis tvs sized manga noticed socket silent literary egg mhz signals caps orientation pill theft childhood swing symbols lat meta humans analog facial choosing talent dated flexibility seeker wisdom shoot boundary mint packard offset payday philip elite gi spin holders believes swedish poems deadline jurisdiction robot displaying witness collins equipped stages encouraged sur winds powder broadway acquired assess wash cartridges stones entrance gnome roots declaration losing attempts gadgets noble glasgow automation impacts rev gospel advantages shore loves induced ll knight preparing loose aims recipient linking extensions appeals cl earned illness islamic athletics southeast ieee ho alternatives pending parker determining lebanon corp personalized kennedy gt sh conditioning teenage soap ae triple cooper nyc vincent jam secured unusual answered partnerships destruction slots increasingly migration disorder routine toolbar basically rocks conventional titans applicants wearing axis sought genes mounted habitat firewall median guns scanner herein occupational animated horny judicial rio hs adjustment hero integer treatments bachelor attitude camcorders engaged falling basics montreal carpet rv struct lenses binary genetics attended difficulty punk collective coalition pi dropped enrollment duke walter ai pace besides wage producers ot collector arc hosts interfaces advertisers moments atlas strings dawn representing observation feels torture carl deleted coat mitchell mrs rica restoration convenience returning ralph opposition container yr defendant warner confirmation app embedded inkjet supervisor wizard corps actors liver peripherals liable brochure morris bestsellers petition eminem recall antenna picked assumed departure minneapolis belief killing bikini memphis shoulder decor lookup texts harvard brokers roy ion diameter ottawa doll ic podcast tit seasons peru interactions refine bidder singer evans herald literacy fails aging nike intervention pissing fed plugin attraction diving invite modification alice latinas suppose customized reed involve moderate terror younger thirty mice opposite understood rapidly dealtime ban temp intro mercedes zus assurance fisting clerk happening vast mills outline amendments tramadol holland receives jeans metropolitan compilation verification fonts ent odd wrap refers mood favor veterans quiz mx sigma gr attractive xhtml occasion recordings jefferson victim demands sleeping careful ext beam gardening obligations arrive orchestra sunset tracked moreover minimal polyphonic lottery tops framed aside outsourcing licence adjustable allocation michelle essay discipline amy ts demonstrated dialogue identifying alphabetical camps declared dispatched aaron handheld trace disposal shut florists packs ge installing switches romania voluntary ncaa thou consult phd greatly blogging mask cycling midnight ng commonly pe photographer inform turkish coal cry messaging pentium quantum murray intent tt zoo largely pleasant announce constructed additions requiring spoke aka arrow engagement sampling rough weird tee refinance lion inspired holes weddings blade suddenly oxygen cookie meals canyon goto meters merely calendars arrangement conclusions passes bibliography pointer compatibility stretch durham furthermore permits cooperative muslim xl neil sleeve netscape cleaner cricket beef feeding stroke township rankings measuring cad hats robin robinson jacksonville strap headquarters sharon crowd tcp transfers surf olympic transformation remained attachments dv dir entities customs administrators personality rainbow hook roulette decline gloves israeli medicare cord skiing cloud facilitate subscriber valve val hewlett explains proceed flickr feelings knife jamaica priorities shelf bookstore timing liked parenting adopt denied fotos incredible britney freeware fucked donation outer crop deaths rivers commonwealth pharmaceutical manhattan tales katrina workforce islam nodes tu fy thumbs seeds cited lite ghz hub targeted organizational skype realized twelve founder decade gamecube rr dispute portuguese tired titten adverse everywhere excerpt eng steam discharge ef drinks ace voices acute halloween climbing stood sing tons perfume carol honest albany hazardous restore stack methodology somebody sue ep housewares reputation resistant democrats recycling hang gbp curve creator amber qualifications museums coding slideshow tracker variation passage transferred trunk hiking lb damn pierre jelsoft headset photograph oakland colombia waves camel distributor lamps underlying hood wrestling suicide archived photoshop jp chi bt arabia gathering projection juice chase mathematical logical sauce fame extract specialized diagnostic panama indianapolis af payable corporations courtesy criticism automobile confidential rfc statutory accommodations athens northeast downloaded judges sl seo retired isp remarks detected decades paintings walked arising nissan bracelet ins eggs juvenile injection yorkshire populations protective afraid acoustic railway cassette initially indicator pointed hb jpg causing mistake norton locked eliminate tc fusion mineral sunglasses ruby steering beads fortune preference canvas threshold parish claimed screens cemetery planner croatia flows stadium venezuela exploration mins fewer sequences coupon nurses ssl stem proxy gangbang astronomy lanka opt edwards drew contests flu translate announces mlb costume tagged berkeley voted killer bikes gates adjusted rap tune bishop pulled corn gp shaped compression seasonal establishing farmer counters puts constitutional grew perfectly tin slave instantly cultures norfolk coaching examined trek encoding litigation submissions oem heroes painted lycos ir zdnet broadcasting horizontal artwork cosmetic resulted portrait terrorist informational ethical carriers ecommerce mobility floral builders ties struggle schemes suffering neutral fisher rat spears prospective dildos bedding ultimately joining heading equally artificial bearing spectacular coordination connector brad combo seniors worlds guilty affiliated activation naturally haven tablet jury dos tail subscribers charm lawn violent mitsubishi underwear basin soup potentially ranch constraints crossing inclusive dimensional cottage drunk considerable crimes resolved mozilla byte toner nose latex branches anymore oclc delhi holdings alien locator selecting processors pantyhose plc broke nepal zimbabwe difficulties juan complexity msg constantly browsing resolve barcelona presidential documentary cod territories melissa moscow thesis thru jews nylon palestinian discs rocky bargains frequent trim nigeria ceiling pixels ensuring hispanic cv cb legislature hospitality gen anybody procurement diamonds espn fleet untitled bunch totals marriott singing theoretical afford exercises starring referral nhl surveillance optimal quit distinct protocols lung highlight substitute inclusion hopefully brilliant turner sucking cents reuters ti fc gel todd spoken omega evaluated stayed civic assignments fw manuals doug sees termination watched saver thereof grill households gs redeem rogers grain aaa authentic regime wanna wishes bull montgomery architectural louisville depend differ macintosh movements ranging monica repairs breath amenities virtually cole mart candle hanging colored authorization tale verified lynn formerly projector bp situated comparative std seeks herbal loving strictly routing docs stanley psychological surprised retailer vitamins elegant gains renewal vid genealogy opposed deemed scoring expenditure panties brooklyn liverpool sisters critics connectivity spots oo algorithms hacker madrid similarly margin coin bbw solely fake salon collaborative norman fda excluding turbo headed voters cure madonna commander arch ni murphy thinks thats suggestion hdtv soldier phillips asin aimed justin bomb harm interval mirrors spotlight tricks reset brush investigate thy expansys panels repeated assault connecting spare logistics deer kodak tongue bowling tri danish pal monkey proportion filename skirt florence invest honey um analyses drawings significance scenario ye fs lovers atomic approx symposium arabic gauge essentials junction protecting nn faced mat rachel solving transmitted weekends screenshots produces oven ted intensive chains kingston sixth engage deviant noon switching quoted adapters correspondence farms imports supervision cheat bronze expenditures sandy separation testimony suspect celebrities macro sender mandatory boundaries crucial syndication gym celebration kde adjacent filtering tuition spouse exotic viewer signup threats luxembourg puzzles reaching vb damaged cams receptor piss laugh joel surgical destroy citation pitch autos yo premises perry proved offensive imperial dozen benjamin deployment teeth cloth studying colleagues stamp lotus salmon olympus separated proc cargo tan directive fx salem mate dl starter upgrades likes butter pepper weapon luggage burden chef tapes zones races isle stylish slim maple luke grocery offshore governing retailers depot kenneth comp alt pie blend harrison ls julie occasionally cbs attending emission pete spec finest realty janet bow penn recruiting apparent instructional phpbb autumn traveling probe midi permissions biotechnology toilet ranked jackets routes packed excited outreach helen mounting recover tied lopez balanced prescribed catherine timely talked upskirts debug delayed chuck reproduced hon dale explicit calculation villas ebook consolidated boob exclude peeing occasions brooks equations newton oils sept exceptional anxiety bingo whilst spatial respondents unto lt ceramic prompt precious minds annually considerations scanners atm xanax eq pays cox fingers sunny ebooks delivers je queensland necklace musicians leeds composite unavailable cedar arranged lang theaters advocacy raleigh stud fold essentially designing threaded uv qualify fingering blair hopes assessments cms mason diagram burns pumps slut ejaculation footwear sg vic beijing peoples victor mario pos attach licenses utils removing advised brunswick spider phys ranges pairs sensitivity trails preservation hudson isolated calgary interim assisted divine streaming approve chose compound intensity technological syndicate abortion dialog venues blast wellness calcium newport antivirus addressing pole discounted indians shield harvest membrane prague previews bangladesh constitute locally concluded pickup desperate mothers nascar iceland demonstration governmental manufactured candles graduation mega bend sailing variations moms sacred addiction morocco chrome tommy springfield refused brake exterior greeting ecology oliver congo glen botswana nav delays synthesis olive undefined unemployment cyber verizon scored enhancement newcastle clone dicks velocity lambda relay composed tears performances oasis baseline cab angry fa societies silicon brazilian identical petroleum compete ist norwegian lover belong honolulu beatles lips escort retention exchanges pond rolls thomson barnes soundtrack wondering malta daddy lc ferry rabbit profession seating dam cnn separately physiology lil collecting das exports omaha tire participant scholarships recreational dominican chad electron loads friendship heather passport motel unions treasury warrant sys solaris frozen occupied josh royalty scales rally observer sunshine strain drag ceremony somehow arrested expanding provincial investigations icq ripe yamaha rely medications hebrew gained rochester dying laundry stuck solomon placing stops homework adjust assessed advertiser enabling encryption filling downloadable sophisticated imposed silence scsi focuses soviet possession cu laboratories treaty vocal trainer organ stronger volumes advances vegetables lemon toxic dns thumbnails darkness pty ws nuts nail bizrate vienna implied span stanford sox stockings joke respondent packing statute rejected satisfy destroyed shelter chapel gamespot manufacture layers wordpress guided vulnerability accountability celebrate accredited appliance compressed bahamas powell mixture zoophilia bench univ tub rider scheduling radius perspectives mortality logging hampton christians borders therapeutic pads butts inns bobby impressive sheep accordingly architect railroad lectures challenging wines nursery harder cups ash microwave cheapest accidents travesti relocation stuart contributors salvador ali salad np monroe tender violations foam temperatures paste clouds competitions discretion tft tanzania preserve jvc poem vibrator unsigned staying cosmetics easter theories repository praise jeremy venice jo concentrations vibrators estonia christianity veteran streams landing signing executed katie negotiations realistic dt cgi showcase integral asks relax namibia generating christina congressional synopsis hardly prairie reunion composer bean sword absent photographic sells ecuador hoping accessed spirits modifications coral pixel float colin bias imported paths bubble por acquire contrary millennium tribune vessel acids focusing viruses cheaper admitted dairy admit mem fancy equality samoa gc achieving tap stickers fisheries exceptions reactions leasing lauren beliefs ci macromedia companion squad analyze ashley scroll relate divisions swim wages additionally suffer forests fellowship nano invalid concerts martial males victorian retain colours execute tunnel genres cambodia patents copyrights yn chaos lithuania mastercard wheat chronicles obtaining beaver updating distribute readings decorative kijiji confused compiler enlargement eagles bases vii accused bee campaigns unity loud conjunction bride rats defines airports instances indigenous begun cfr brunette packets anchor socks validation parade corruption stat trigger incentives cholesterol gathered essex slovenia notified differential beaches folders dramatic surfaces terrible routers cruz pendant dresses baptist scientist starsmerchant hiring clocks arthritis bios females wallace nevertheless reflects taxation fever pmc cuisine surely practitioners transcript myspace theorem inflation thee nb ruth pray stylus compounds pope drums contracting topless arnold structured reasonably jeep chicks bare hung cattle mba radical graduates rover recommends controlling treasure reload distributors flame levitra tanks assuming monetary elderly pit arlington mono particles floating extraordinary tile indicating bolivia spell hottest stevens coordinate kuwait exclusively emily alleged limitation widescreen compile squirting webster struck rx illustration plymouth warnings construct apps inquiries bridal annex mag gsm inspiration tribal curious affecting freight rebate meetup eclipse sudan ddr downloading rec shuttle aggregate stunning cycles affects forecasts detect sluts actively ciao ampland knee prep pb complicated chem fastest butler shopzilla injured decorating payroll cookbook expressions ton courier uploaded shakespeare hints collapse americas connectors twinks unlikely oe gif pros conflicts techno beverage tribute wired elvis immune latvia travelers forestry barriers cant jd rarely gpl infected offerings martha genesis barrier argue incorrect trains metals bicycle furnishings letting arise guatemala celtic thereby irc jamie particle perception minerals advise humidity bottles boxing wy dm bangkok renaissance pathology sara bra ordinance hughes photographers bitch infections jeffrey chess operates brisbane configured survive oscar festivals menus joan possibilities duck reveal canal amino phi contributing herbs clinics mls cow manitoba analytical missions watson lying costumes strict dive saddam circulation drill offense threesome bryan cet protest handjob assumption jerusalem hobby tries transexuales invention nickname fiji technician inline executives enquiries washing audi staffing cognitive exploring trick enquiry closure raid ppc timber volt intense div playlist registrar showers supporters ruling steady dirt statutes withdrawal myers drops predicted wider saskatchewan jc cancellation plugins enrolled sensors screw ministers publicly hourly blame geneva freebsd veterinary acer prostores reseller dist handed suffered intake informal relevance incentive butterfly tucson mechanics heavily swingers fifty headers mistakes numerical ons geek uncle defining xnxx counting reflection sink accompanied assure invitation devoted princeton jacob sodium randy spirituality hormone meanwhile proprietary timothy childrens brick grip naval thumbzilla medieval porcelain avi bridges pichunter captured watt thehun decent casting dayton translated shortly cameron columnists pins carlos reno donna andreas warrior diploma cabin innocent bdsm scanning ide consensus polo valium copying rpg delivering cordless patricia horn eddie uganda fired journalism pd prot trivia adidas perth frog grammar intention syria disagree klein harvey tires logs undertaken tgp hazard retro leo livesex statewide semiconductor gregory episodes boolean circular anger diy mainland illustrations suits chances interact snap happiness arg substantially bizarre glenn ur auckland olympics fruits identifier geo worldsex ribbon calculations doe jpeg conducting startup suzuki trinidad ati kissing wal handy swap exempt crops reduces accomplished calculators geometry impression abs slovakia flip guild correlation gorgeous capitol sim dishes rna barbados chrysler nervous refuse extends fragrance mcdonald replica plumbing brussels tribe neighbors trades superb buzz transparent nuke rid trinity charleston handled legends boom calm champions floors selections projectors inappropriate exhaust comparing shanghai speaks burton vocational davidson copied scotia farming gibson pharmacies fork troy ln roller introducing batch organize appreciated alter nicole latino ghana edges uc mixing handles skilled fitted albuquerque harmony distinguished asthma projected assumptions shareholders twins developmental rip zope regulated triangle amend anticipated oriental reward windsor zambia completing gmbh buf ld hydrogen webshots sprint comparable chick advocate sims confusion copyrighted tray inputs warranties genome escorts documented thong medal paperbacks coaches vessels harbour walks sucks sol keyboards sage knives eco vulnerable arrange artistic bat honors booth indie reflected unified bones breed detector ignored polar fallen precise sussex respiratory notifications msgid transexual mainstream invoice evaluating lip subcommittee sap gather suse maternity backed alfred colonial mf carey motels forming embassy cave journalists danny rebecca slight proceeds indirect amongst wool foundations msgstr arrest volleyball mw adipex horizon nu deeply toolbox ict marina liabilities prizes bosnia browsers decreased patio dp tolerance surfing creativity lloyd describing optics pursue lightning overcome eyed ou quotations grab inspector attract brighton beans bookmarks ellis disable snake succeed leonard lending oops reminder nipple xi searched behavioral riverside bathrooms plains sku ht raymond insights abilities initiated sullivan za midwest karaoke trap lonely fool ve nonprofit lancaster suspended hereby observe julia containers attitudes karl berry collar simultaneously racial integrate bermuda amanda sociology mobiles screenshot exhibitions kelkoo confident retrieved exhibits officially consortium dies terrace bacteria pts replied seafood novels rh rrp recipients playboy ought delicious traditions fg jail safely finite kidney periodically fixes sends durable mazda allied throws moisture hungarian roster referring symantec spencer wichita nasdaq uruguay ooo hz transform timer tablets tuning gotten educators tyler futures vegetable verse highs humanities independently wanting custody scratch launches ipaq alignment masturbating henderson bk britannica comm ellen competitors nhs rocket aye bullet towers racks lace nasty visibility latitude consciousness ste tumor ugly deposits beverly mistress encounter trustees watts duncan reprints hart bernard resolutions ment accessing forty tubes attempted col midlands priest floyd ronald analysts queue dx sk trance locale nicholas biol yu bundle hammer invasion witnesses runner rows administered notion sq skins mailed oc fujitsu spelling arctic exams rewards beneath strengthen defend aj frederick medicaid treo infrared seventh gods une welsh belly aggressive tex advertisements quarters stolen cia sublimedirectory soonest haiti disturbed determines sculpture poly ears dod wp fist naturals neo motivation lenders pharmacology fitting fixtures bloggers mere agrees passengers quantities petersburg consistently powerpoint cons surplus elder sonic obituaries cheers dig taxi punishment appreciation subsequently om belarus nat zoning gravity providence thumb restriction incorporate backgrounds treasurer guitars essence flooring lightweight ethiopia tp mighty athletes humanity transcription jm holmes complications scholars dpi scripting gis remembered galaxy chester snapshot caring loc worn synthetic shaw vp segments testament expo dominant twist specifics itunes stomach partially buried cn newbie minimize darwin ranks wilderness debut generations tournaments bradley deny anatomy bali judy sponsorship headphones fraction trio proceeding cube defects volkswagen uncertainty breakdown milton marker reconstruction subsidiary strengths clarity rugs sandra adelaide encouraging furnished monaco settled folding emirates terrorists airfare comparisons beneficial distributions vaccine belize crap fate viewpicture promised volvo penny robust bookings threatened minolta republicans discusses gui porter gras jungle ver rn responded rim abstracts zen ivory alpine dis prediction pharmaceuticals andale fabulous remix alias thesaurus individually battlefield literally newer kay ecological spice oval implies cg soma ser cooler appraisal consisting maritime periodic submitting overhead ascii prospect shipment breeding citations geographical donor mozambique tension href benz trash shapes wifi tier fwd earl manor envelope diane homeland disclaimers championships excluded andrea breeds rapids disco sheffield bailey aus endif finishing emotions wellington incoming prospects lexmark cleaners bulgarian hwy eternal cashiers guam cite aboriginal remarkable rotation nam preventing productive boulevard eugene ix gdp pig metric compliant minus penalties bennett imagination hotmail refurbished joshua armenia varied grande closest activated actress mess conferencing assign armstrong politicians trackbacks lit accommodate tigers aurora una slides milan premiere lender villages shade chorus christine rhythm digit argued dietary symphony clarke sudden accepting precipitation marilyn lions findlaw ada pools tb lyric claire isolation speeds sustained matched approximate rope carroll rational programmer fighters chambers dump greetings inherited warming incomplete vocals chronicle fountain chubby grave legitimate biographies burner yrs foo investigator gba plaintiff finnish gentle bm prisoners deeper muslims hose mediterranean nightlife footage howto worthy reveals architects saints entrepreneur carries sig freelance duo excessive devon screensaver helena saves regarded valuation unexpected cigarette fog characteristic marion lobby egyptian tunisia metallica outlined consequently headline treating punch appointments str gotta cowboy narrative bahrain enormous karma consist betty queens academics pubs quantitative shemales lucas screensavers subdivision tribes vip defeat clicks distinction honduras naughty hazards insured harper livestock mardi exemption tenant sustainability cabinets tattoo shake algebra shadows holly formatting silly nutritional yea mercy hartford freely marcus sunrise wrapping mild fur nicaragua weblogs timeline tar belongs rj readily affiliation soc fence nudist infinite diana ensures relatives lindsay clan legally shame satisfactory revolutionary bracelets sync civilian telephony mesa fatal remedy realtors breathing briefly thickness adjustments graphical genius discussing aerospace fighter meaningful flesh retreat adapted barely wherever estates rug democrat borough maintains failing shortcuts ka retained voyeurweb pamela andrews marble extending jesse specifies hull logitech surrey briefing belkin dem accreditation wav blackberry highland meditation modular microphone macedonia combining brandon instrumental giants organizing shed balloon moderators winston memo ham solved tide kazakhstan hawaiian standings partition invisible gratuit consoles funk fbi qatar magnet translations porsche cayman jaguar reel sheer commodity posing wang kilometers rp bind thanksgiving rand hopkins urgent guarantees infants gothic cylinder witch buck indication eh congratulations tba cohen sie usgs puppy kathy acre graphs surround cigarettes revenge expires enemies lows controllers aqua chen emma consultancy finances accepts enjoying conventions eva patrol smell pest hc italiano coordinates rca fp carnival roughly sticker promises responding reef physically divide stakeholders hydrocodone gst consecutive cornell satin bon deserve attempting mailto promo jj representations chan worried tunes garbage competing combines mas beth bradford len phrases kai peninsula chelsea boring reynolds dom jill accurately speeches reaches schema considers sofa catalogs ministries vacancies quizzes parliamentary obj prefix lucia savannah barrel typing nerve dans planets deficit boulder pointing renew coupled viii myanmar metadata harold circuits floppy texture handbags jar ev somerset incurred acknowledge thoroughly antigua nottingham thunder tent caution identifies questionnaire qualification locks modelling namely miniature dept hack dare euros interstate pirates aerial hawk consequence rebel systematic perceived origins hired makeup textile lamb madagascar nathan tobago presenting cos troubleshooting uzbekistan indexes pac rl erp centuries gl magnitude ui richardson hindu dh fragrances vocabulary licking earthquake vpn fundraising fcc markers weights albania geological assessing lasting wicked eds introduces kills roommate webcams pushed webmasters ro df computational acdbentity participated junk handhelds wax lucy answering hans impressed slope reggae failures poet conspiracy surname theology nails evident whats rides rehab epic saturn organizer nut allergy sake twisted combinations preceding merit enzyme cumulative zshops planes edmonton tackle disks condo pokemon amplifier ambien arbitrary prominent retrieve lexington vernon sans worldcat titanium irs fairy builds contacted shaft lean bye cdt recorders occasional leslie casio deutsche ana postings innovations kitty postcards dude drain monte fires algeria blessed luis reviewing cardiff cornwall favors potato panic explicitly sticks leone transsexual ez citizenship excuse reforms basement onion strand pf sandwich uw lawsuit alto informative girlfriend bloomberg cheque hierarchy influenced banners reject eau abandoned bd circles italic beats merry mil scuba gore complement cult dash passive mauritius valued cage checklist bangbus requesting courage verde lauderdale scenarios gazette hitachi divx extraction batman elevation hearings coleman hugh lap utilization beverages calibration jake eval efficiently anaheim ping textbook dried entertaining prerequisite luther frontier settle stopping refugees knights hypothesis palmer medicines flux derby sao peaceful altered pontiac regression doctrine scenic trainers muze enhancements renewable intersection passwords sewing consistency collectors conclude recognised munich oman celebs gmc propose hh azerbaijan lighter rage adsl uh prix astrology advisors pavilion tactics trusts occurring supplemental travelling talented annie pillow induction derek precisely shorter harley spreading provinces relying finals paraguay steal parcel refined fd bo fifteen widespread incidence fears predict boutique acrylic rolled tuner avon incidents peterson rays asn shannon toddler enhancing flavor alike walt homeless horrible hungry metallic acne blocked interference warriors palestine listprice libs undo cadillac atmospheric malawi wm pk sagem knowledgestorm dana halo ppm curtis parental referenced strikes lesser publicity marathon ant proposition gays pressing gasoline apt dressed scout belfast exec dealt niagara inf eos warcraft charms catalyst trader bucks allowance vcr denial uri designation thrown prepaid raises gem duplicate electro criterion badge wrist civilization analyzed vietnamese heath tremendous ballot lexus varying remedies validity trustee maui handjobs weighted angola squirt performs plastics realm corrected jenny helmet salaries postcard elephant yemen encountered tsunami scholar nickel internationally surrounded psi buses expedia geology pct wb creatures coating commented wallet cleared smilies vids accomplish boating drainage shakira corners broader vegetarian rouge yeast yale newfoundland sn qld pas clearing investigated dk ambassador coated intend stephanie contacting vegetation doom findarticles louise kenny specially owen routines hitting yukon beings bite issn aquatic reliance habits striking myth infectious podcasts singh gig gilbert sas ferrari continuity brook fu outputs phenomenon ensemble insulin assured biblical weed conscious accent mysimon eleven wives ambient utilize mileage oecd prostate adaptor auburn unlock hyundai pledge vampire angela relates nitrogen xerox dice merger softball referrals quad dock differently firewire mods nextel framing organised musician blocking rwanda sorts integrating vsnet limiting dispatch revisions papua restored hint armor riders chargers remark dozens varies msie reasoning wn liz rendered picking charitable guards annotated ccd sv convinced openings buys burlington replacing researcher watershed councils occupations acknowledged nudity kruger pockets granny pork zu equilibrium viral inquire pipes characterized laden aruba cottages realtor merge privilege edgar develops qualifying chassis dubai estimation barn pushing llp fleece pediatric boc fare dg asus pierce allan dressing techrepublic sperm vg bald filme craps fuji frost leon institutes mold dame fo sally yacht tracy prefers drilling brochures herb tmp alot ate breach whale traveller appropriations suspected tomatoes benchmark beginners instructors highlighted bedford stationery idle mustang unauthorized clusters antibody competent momentum fin wiring io pastor mud calvin uni shark contributor demonstrates phases grateful emerald gradually laughing grows cliff desirable tract ul ballet ol journalist abraham js bumper afterwards webpage religions garlic hostels shine senegal explosion pn banned wendy briefs signatures diffs cove mumbai ozone disciplines casa mu daughters conversations radios tariff nvidia opponent pasta simplified muscles serum wrapped swift motherboard runtime inbox focal bibliographic vagina eden distant incl champagne ala decimal hq deviation superintendent propecia dip nbc samba hostel housewives employ mongolia penguin magical influences inspections irrigation miracle manually reprint reid wt hydraulic centered robertson flex yearly penetration wound belle rosa conviction hash omissions writings hamburg lazy mv mpg retrieval qualities cindy lolita fathers carb charging cas marvel lined cio dow prototype importantly rb petite apparatus upc terrain dui pens explaining yen strips gossip rangers nomination empirical mh rotary worm dependence discrete beginner boxed lid sexuality polyester cubic deaf commitments suggesting sapphire kinase skirts mats remainder crawford labeled privileges televisions specializing marking commodities pvc serbia sheriff griffin declined guyana spies blah mime neighbor motorcycles elect highways thinkpad concentrate intimate reproductive preston deadly cunt feof bunny chevy molecules rounds longest refrigerator tions intervals sentences dentists usda exclusion workstation holocaust keen flyer peas dosage receivers urls customise disposition variance navigator investigators cameroon baking marijuana adaptive computed needle baths enb gg cathedral brakes og nirvana ko fairfield owns til invision sticky destiny generous madness emacs climb blowing fascinating landscapes heated lafayette jackie wto computation hay cardiovascular ww sparc cardiac salvation dover adrian predictions accompanying vatican brutal learners gd selective arbitration configuring token editorials zinc sacrifice seekers guru isa removable convergence yields gibraltar levy suited numeric anthropology skating kinda aberdeen emperor grad malpractice dylan bras belts blacks educated rebates reporters burke proudly pix necessity rendering mic inserted pulling basename kyle obesity curves suburban touring clara vertex bw hepatitis nationally tomato andorra waterproof expired mj travels flush waiver pale specialties hayes humanitarian invitations functioning delight survivor garcia cingular economies alexandria bacterial moses counted undertake declare continuously johns valves gaps impaired achievements donors tear jewel teddy lf convertible ata teaches ventures nil bufing stranger tragedy julian nest pam dryer painful velvet tribunal ruled nato pensions prayers funky secretariat nowhere cop paragraphs gale joins adolescent nominations wesley dim lately cancelled scary mattress mpegs brunei likewise banana introductory slovak cakes stan reservoir occurrence idol bloody mixer remind wc worcester sbjct demographic charming mai tooth disciplinary annoying respected stays disclose affair drove washer upset restrict springer beside mines portraits rebound logan mentor interpreted evaluations fought baghdad elimination metres hypothetical immigrants complimentary helicopter pencil freeze hk performer abu titled commissions sphere powerseller moss ratios concord graduated endorsed ty surprising walnut lance ladder italia unnecessary dramatically liberia sherman cork maximize cj hansen senators workout mali yugoslavia bleeding characterization colon likelihood lanes purse fundamentals contamination mtv endangered compromise masturbation optimize stating dome caroline leu expiration namespace align peripheral bless engaging negotiation crest opponents triumph nominated confidentiality electoral changelog welding orgasm deferred alternatively heel alloy condos plots polished yang gently greensboro tulsa locking casey controversial draws fridge blanket bloom qc simpsons lou elliott recovered fraser justify upgrading blades pgp loops surge frontpage trauma aw tahoe advert possess demanding defensive sip flashers subaru forbidden tf vanilla programmers pj monitored installations deutschland picnic souls arrivals spank cw practitioner motivated wr dumb smithsonian hollow vault securely examining fioricet groove revelation rg pursuit delegation wires bl dictionaries mails backing greenhouse sleeps vc blake transparency dee travis wx endless figured orbit currencies niger bacon survivors positioning heater colony cannon circus promoted forbes mae moldova mel descending paxil spine trout enclosed feat temporarily ntsc cooked thriller transmit apnic fatty gerald pressed frequencies scanned reflections hunger mariah sic municipality usps joyce detective surgeon cement experiencing fireplace endorsement bg planners disputes textiles missile intranet closes seq psychiatry persistent deborah conf marco assists summaries glow gabriel auditor wma aquarium violin prophet cir bracket looksmart isaac oxide oaks magnificent erik colleague naples promptly modems adaptation hu harmful paintball prozac sexually enclosure acm dividend newark kw paso glucose phantom norm playback supervisors westminster turtle ips distances absorption treasures dsc warned neural ware fossil mia hometown badly transcripts apollo wan disappointed persian continually communist collectible handmade greene entrepreneurs robots grenada creations jade scoop acquisitions foul keno gtk earning mailman sanyo nested biodiversity excitement somalia movers verbal blink presently seas carlo workflow mysterious novelty bryant tiles voyuer librarian subsidiaries switched stockholm tamil garmin ru pose fuzzy indonesian grams therapist richards mrna budgets toolkit promising relaxation goat render carmen ira sen thereafter hardwood erotica temporal sail forge commissioners dense dts brave forwarding qt awful nightmare airplane reductions southampton istanbul impose organisms sega telescope viewers asbestos portsmouth cdna meyer enters pod savage advancement wu harassment willow resumes bolt gage throwing existed whore generators lu wagon barbie dat favour soa knock urge smtp generates potatoes thorough replication inexpensive kurt receptors peers roland optimum neon interventions quilt huntington creature ours mounts syracuse internship lone refresh aluminium snowboard beastality webcast michel evanescence subtle coordinated notre shipments maldives stripes firmware antarctica cope shepherd lm canberra cradle chancellor mambo lime kirk flour controversy legendary bool sympathy choir avoiding beautifully blond expects cho jumping fabrics antibodies polymer hygiene wit poultry virtue burst examinations surgeons bouquet immunology promotes mandate wiley departmental bbs spas ind corpus johnston terminology gentleman fibre reproduce convicted shades jets indices roommates adware qui intl threatening spokesman zoloft activists frankfurt prisoner daisy halifax encourages ultram cursor assembled earliest donated stuffed restructuring insects terminals crude morrison maiden simulations cz sufficiently examines viking myrtle bored cleanup yarn knit conditional mug crossword bother budapest conceptual knitting attacked hl bhutan liechtenstein mating compute redhead arrives translator automobiles tractor allah continent ob unwrap fares longitude resist challenged telecharger hoped pike safer insertion instrumentation ids hugo wagner constraint groundwater touched strengthening cologne gzip wishing ranger smallest insulation newman marsh ricky ctrl scared theta infringement bent laos subjective monsters asylum lightbox robbie stake cocktail outlets swaziland varieties arbor mediawiki configurations poison""".split())

def caesar_encrypt(text, shift):
    return ''.join(
        chr((ord(c)-65+shift)%26+65) if c.isupper() else
        chr((ord(c)-97+shift)%26+97) if c.islower() else c
        for c in text
    )

def caesar_bruteforce(text):
    best_shift, best_score, best_text = 0, -1, text
    for s in range(26):
        decrypted = caesar_encrypt(text, -s)
        words = [w.strip(string.punctuation).lower() for w in decrypted.split()]
        score = sum(1 for w in words if w in ENGLISH_WORDS)
        if score > best_score:
            best_shift, best_score, best_text = s, score, decrypted
    return f"Best shift: {best_shift}\n{best_text}"

def rot13(text):
    return ''.join(
        chr((ord(c)-65+13)%26+65) if c.isupper() else
        chr((ord(c)-97+13)%26+97) if c.islower() else c
        for c in text
    )

def atbash(text):
    return ''.join(
        chr(90-(ord(c)-65)) if c.isupper() else
        chr(122-(ord(c)-97)) if c.islower() else c
        for c in text
    )

def vigenere_encrypt(text,key):
    key=key.lower()
    res=[]
    ki=0
    for c in text:
        if c.isalpha():
            offset=ord(key[ki%len(key)])-97
            if c.isupper(): res.append(chr((ord(c)-65+offset)%26+65))
            else: res.append(chr((ord(c)-97+offset)%26+97))
            ki+=1
        else: res.append(c)
    return ''.join(res)

def vigenere_decrypt(text,key):
    key=key.lower()
    res=[]
    ki=0
    for c in text:
        if c.isalpha():
            offset=ord(key[ki%len(key)])-97
            if c.isupper(): res.append(chr((ord(c)-65-offset)%26+65))
            else: res.append(chr((ord(c)-97-offset)%26+97))
            ki+=1
        else: res.append(c)
    return ''.join(res)

def affine_encrypt(text,a,b):
    return ''.join(
        chr(((a*(ord(c)-65)+b)%26)+65) if c.isupper() else
        chr(((a*(ord(c)-97)+b)%26)+97) if c.islower() else c
        for c in text
    )

def affine_decrypt(text,a,b):
    def modinv(a,m):
        for i in range(1,m):
            if (a*i)%m==1: return i
        return None
    a_inv=modinv(a,26)
    if a_inv is None: return "Invalid key for Affine"
    return ''.join(
        chr((a_inv*(ord(c)-65-b))%26+65) if c.isupper() else
        chr((a_inv*(ord(c)-97-b))%26+97) if c.islower() else c
        for c in text
    )

def rail_fence_encrypt(text,rails):
    if rails<2: return text
    fence=[[] for _ in range(rails)]
    rail=0
    dir=1
    for c in text:
        fence[rail].append(c)
        rail+=dir
        if rail==0 or rail==rails-1: dir*=-1
    return ''.join(''.join(row) for row in fence)

def rail_fence_decrypt(text,rails):
    if rails<2: return text
    n=len(text)
    pattern=[]
    rail,dir=0,1
    for i in range(n):
        pattern.append(rail)
        rail+=dir
        if rail==0 or rail==rails-1: dir*=-1
    fence=[[] for _ in range(rails)]
    idx=[0]*rails
    counts=[pattern.count(r) for r in range(rails)]
    start=0
    for r in range(rails):
        fence[r]=list(text[start:start+counts[r]])
        start+=counts[r]
    res=''
    for p in pattern:
        res+=fence[p][idx[p]]
        idx[p]+=1
    return res

def columnar_encrypt(text,key):
    k_len=len(key)
    n_rows=(len(text)+k_len-1)//k_len
    matrix=[list(text[i*k_len:(i+1)*k_len])+['']*(k_len-len(text[i*k_len:(i+1)*k_len])) for i in range(n_rows)]
    order=[i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    res=''
    for c in order:
        for r in range(n_rows):
            if matrix[r][c]!='': res+=matrix[r][c]
    return res

def columnar_decrypt(text,key):
    k_len=len(key)
    n_rows=(len(text)+k_len-1)//k_len
    order=[i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    matrix=[['']*k_len for _ in range(n_rows)]
    idx=0
    for c in order:
        for r in range(n_rows):
            if idx<len(text):
                matrix[r][c]=text[idx]
                idx+=1
    return ''.join(''.join(row).strip() for row in matrix)

# --- Playfair Cipher ---
def playfair_square(key):
    key = ''.join(sorted(set(key), key=key.index)).replace('j','i')
    alpha = ''.join([c for c in string.ascii_lowercase if c != 'j'])
    square = key + ''.join([c for c in alpha if c not in key])
    return [list(square[i*5:(i+1)*5]) for i in range(5)]

def playfair_prepare(text):
    text = text.lower().replace('j','i')
    text = ''.join([c for c in text if c.isalpha()])
    res = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            res += a + 'x'
            i += 1
        else:
            res += a + b
            i += 2
    if len(res) % 2: res += 'x'
    return res

def playfair_encrypt(text, key):
    square = playfair_square(key)
    text = playfair_prepare(text)
    res = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        ax, ay = [(ix, iy) for ix,row in enumerate(square) for iy,c in enumerate(row) if c==a][0]
        bx, by = [(ix, iy) for ix,row in enumerate(square) for iy,c in enumerate(row) if c==b][0]
        if ax == bx:
            res += square[ax][(ay+1)%5] + square[bx][(by+1)%5]
        elif ay == by:
            res += square[(ax+1)%5][ay] + square[(bx+1)%5][by]
        else:
            res += square[ax][by] + square[bx][ay]
    return res.upper()

def playfair_decrypt(text, key):
    square = playfair_square(key)
    text = text.lower()
    if len(text) % 2:
        text += 'x'
    res = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        ax, ay = [(ix, iy) for ix,row in enumerate(square) for iy,c in enumerate(row) if c==a][0]
        bx, by = [(ix, iy) for ix,row in enumerate(square) for iy,c in enumerate(row) if c==b][0]
        if ax == bx:
            res += square[ax][(ay-1)%5] + square[bx][(by-1)%5]
        elif ay == by:
            res += square[(ax-1)%5][ay] + square[(bx-1)%5][by]
        else:
            res += square[ax][by] + square[bx][ay]
    return res

# --- Hill Cipher ---
def hill_encrypt(text, key):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    while len(text) % len(key) != 0:
        text += 'x'
    key_matrix = np.array([[ord(c)-97 for c in row] for row in key])
    res = ''
    for i in range(0, len(text), len(key)):
        block = np.array([[ord(c)-97] for c in text[i:i+len(key)]])
        enc = np.dot(key_matrix, block) % 26
        res += ''.join(chr(int(n)+97) for n in enc.flatten())
    return res

def hill_decrypt(text, key):
    key_matrix = np.array([[ord(c)-97 for c in row] for row in key])
    det = int(round(np.linalg.det(key_matrix)))
    # Validate invertibility modulo 26
    if math.gcd(det % 26, 26) != 1:
        return "Invalid key matrix (not invertible modulo 26)."
    try:
        det_inv = pow(det, -1, 26)
    except ValueError:
        return "Invalid key matrix (no modular inverse)."
    key_matrix_inv = det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    res = ''
    for i in range(0, len(text), len(key)):
        block = np.array([[ord(c)-97] for c in text[i:i+len(key)]])
        dec = np.dot(key_matrix_inv, block) % 26
        res += ''.join(chr(int(n)+97) for n in dec.flatten())
    return res

# --- Bacon Cipher ---
def bacon_encrypt(text):
    bacon = {c:format(i,'05b') for i,c in enumerate(string.ascii_uppercase)}
    return ' '.join(bacon.get(c.upper(),'') for c in text if c.isalpha())

def bacon_decrypt(text):
    bacon = {format(i,'05b'):c for i,c in enumerate(string.ascii_uppercase)}
    return ''.join(bacon.get(b,'') for b in text.split())

# --- Polybius Square ---
def polybius_encrypt(text):
    square = [list('ABCDE'),list('FGHIK'),list('LMNOP'),list('QRSTU'),list('VWXYZ')]
    lookup = {c: f"{i+1}{j+1}" for i,row in enumerate(square) for j,c in enumerate(row)}
    return ' '.join(lookup.get(c.upper(),'') for c in text if c.isalpha())

def polybius_decrypt(text):
    square = [list('ABCDE'),list('FGHIK'),list('LMNOP'),list('QRSTU'),list('VWXYZ')]
    coords = text.split()
    res = ''
    for c in coords:
        if len(c)==2 and c.isdigit():
            i,j = int(c[0])-1, int(c[1])-1
            res += square[i][j]
    return res

# --- Morse Code ---
MORSE = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'
}
def morse_encrypt(text):
    return ' '.join(MORSE.get(c.upper(),'') for c in text if c.upper() in MORSE)

def morse_decrypt(text):
    rev = {v:k for k,v in MORSE.items()}
    return ''.join(rev.get(c,'') for c in text.split())

# --- Scytale Cipher ---
def scytale_encrypt(text, diameter):
    text = text.replace(' ','')
    while len(text) % diameter != 0:
        text += 'X'
    n_rows = len(text)//diameter
    return ''.join(text[i::n_rows] for i in range(n_rows))

def scytale_decrypt(text, diameter):
    n_rows = diameter
    n_cols = len(text)//n_rows
    res = ['']*len(text)
    idx = 0
    for i in range(n_cols):
        for j in range(n_rows):
            if idx < len(text):
                res[j*n_cols+i] = text[idx]
                idx += 1
    return ''.join(res).rstrip('X')

# --- Frequency Analysis ---
def freq_analysis(text):
    text = ''.join(c for c in text.lower() if c.isalpha())
    freq = {c:0 for c in string.ascii_lowercase}
    for c in text:
        freq[c] += 1
    total = sum(freq.values())
    return '\n'.join(f"{c}: {freq[c]} ({freq[c]/total:.2%})" for c in string.ascii_lowercase if freq[c]>0)

# ---------------- GUI ---------------- #
THEMES = ["minty", "cosmo", "flatly", "superhero", "darkly"]
THEME_NAMES = {"minty": "Minty", "cosmo": "Cosmo", "flatly": "Flatly", "superhero": "Superhero", "darkly": "Darkly"}

root = tb.Window(themename="minty")
root.title("Nitz's Ultimate Crypto Cipher Tool")
root.geometry("1000x720")
root.minsize(920, 640)
# Global style tweaks for a modern look
style = tb.Style()

# Helper to create fancy, responsive CTA buttons

def stylize_cta_button(btn, normal_style, hover_style):
    # Avoid setting 'font' on ttk buttons to prevent '-font' option errors.
    btn.configure(cursor="hand2", bootstyle=normal_style)
    def on_enter(e):
        btn.configure(bootstyle=hover_style)
    def on_leave(e):
        btn.configure(bootstyle=normal_style)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
# Set window icon with multiple attempts for Windows taskbar compatibility
def set_window_icon():
    try:
        ico_primary = os.path.join(BASE_DIR, "Classical Encryption App Icon.ico")
        if os.path.exists(ico_primary):
            # Method 1: Use iconbitmap (most reliable for Windows taskbar)
            try:
                root.iconbitmap(ico_primary)
                print("Icon set via iconbitmap")
            except Exception as e:
                print("iconbitmap failed:", e)

            # Method 2: Also set iconphoto for cross-platform compatibility
            try:
                pil_img = Image.open(ico_primary)
                icon_img = ImageTk.PhotoImage(pil_img)
                root.iconphoto(True, icon_img)
                print("Icon set via iconphoto")
            except Exception as e:
                print("iconphoto failed:", e)

            # Method 3: Force Windows to update taskbar (additional attempt)
            try:
                root.update_idletasks()
                # Try setting it again after a short delay
                root.after(100, lambda: root.iconbitmap(ico_primary) if os.path.exists(ico_primary) else None)
            except Exception as e:
                print("Delayed icon set failed:", e)
        else:
            # Fallback to PNG if ICO not found
            png_path = os.path.join(BASE_DIR, "Classical Encryption App Icon.png")
            if os.path.exists(png_path):
                try:
                    icon_img = ImageTk.PhotoImage(Image.open(png_path))
                    root.iconphoto(True, icon_img)
                    print("PNG icon set as fallback")
                except Exception as e:
                    print("PNG icon failed:", e)
    except Exception as e:
        print("Window icon setup failed:", e)

# Set icon immediately
set_window_icon()

# Also try to set it after window is mapped (additional attempt for stubborn Windows)
def set_icon_after_map():
    try:
        ico_primary = os.path.join(BASE_DIR, "Classical Encryption App Icon.ico")
        if os.path.exists(ico_primary):
            root.iconbitmap(ico_primary)
            print("Icon set after window mapped")
    except Exception as e:
        print("Post-map icon set failed:", e)

root.bind('<Map>', lambda e: set_icon_after_map())

# Prepare logo image for placement in topbar later
logo_photo = None
try:
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    logo_candidates = [
        os.path.join(BASE_DIR, "Classical Encryption App Icon.png"),
        os.path.join(BASE_DIR, "app_icon.png"),
        os.path.join(BASE_DIR, "logo.png"),
        os.path.join(BASE_DIR, "Classical Encryption App Icon.ico"),
        os.path.join(downloads_dir, "Classical Encryption App Icon.png"),
        os.path.join(downloads_dir, "Classical Encryption App Icon.ico"),
    ]
    _logo_path = next((p for p in logo_candidates if os.path.exists(p)), None)
    if _logo_path:
        lg = Image.open(_logo_path)
        lg = lg.resize((64, 64), RESAMPLE)
        try:
            from PIL import ImageDraw
            m = Image.new('L', lg.size, 0)
            d = ImageDraw.Draw(m)
            d.rounded_rectangle((0, 0, 64, 64), radius=18, fill=255)
            lg.putalpha(m)
        except Exception:
            pass
        logo_photo = ImageTk.PhotoImage(lg)
except Exception as e:
    print("Logo not prepared:", e)

# Top toolbar with theme selector
topbar = tb.Frame(root)
topbar.pack(fill=X, padx=8, pady=(6,0))
# Add logo on the left if available
if 'logo_photo' in globals() and logo_photo:
    _logo_lbl = tb.Label(topbar, image=logo_photo)
    _logo_lbl.image = logo_photo
    _logo_lbl.pack(side=LEFT, padx=(4,10), pady=0)
    # Brand title beside the logo
    brand_title = tb.Label(topbar, text="ℕ𝕚𝕥𝕫'𝕤 𝕌𝕝𝕥𝕚𝕞𝕒𝕥𝕖 ℂ𝕣𝕪𝕡𝕥𝕠 ℂ𝕚𝕡𝕙𝕖𝕣 𝕋𝕠𝕠𝕝")
    brand_title.pack(side=LEFT, padx=(0,10), pady=0)
# Right-aligned Appearance card (stable across themes)
appearance_card = tb.Labelframe(topbar, text="Appearance", bootstyle=SECONDARY)
appearance_card.pack(side=RIGHT, padx=6, pady=0)
row = tb.Frame(appearance_card)
row.pack(padx=8, pady=6)
tb.Label(row, text="Theme:").pack(side=LEFT, padx=(0,6))
_theme_var = tb.StringVar(value=root.style.theme.name)
_theme_combo = ttk.Combobox(row, textvariable=_theme_var, values=THEMES, state="readonly", width=14)
_theme_combo.pack(side=LEFT)

def _apply_theme(event=None):
    try:
        root.style.theme_use(_theme_var.get())
    except Exception as e:
        print("Theme not applied:", e)

_theme_combo.bind("<<ComboboxSelected>>", _apply_theme)

# Header/title + banner (right-aligned, responsive)
try:
    header_frame = tb.Frame(root)
    header_frame.pack(fill=X, padx=8, pady=(8, 2))

    # Left: fancy Fraktur-style title + subtitle
    header_left = tb.Frame(header_frame)
    header_left.pack(side=LEFT, fill=X, expand=1)
    title_area = tb.Frame(header_left)
    title_area.pack(anchor="w", pady=(4,0), fill=X)
    title_lbl = None
    title_canvas = None
    subtitle_lbl = tb.Label(
        header_left,
        text="Encrypt • Decrypt • Analyze",
        font=("Segoe UI", 10),
        foreground="#6c757d"
    )
    subtitle_lbl.pack(anchor="w", pady=(0,6))

    # Right: banner image (if available) placed to the top-right
    header_right = tb.Frame(header_frame)
    header_right.pack(side=RIGHT, anchor="e")
    banner_label = tb.Label(header_right)
    banner_label.pack(anchor="e", padx=(8,0), pady=(2,2))

    # Using pack for left/right prevents the right banner from being squeezed out

    # Title presentation: marquee when narrow, static label otherwise
    TITLE_TEXT = "𝕮𝖑𝖆𝖘𝖘𝖎𝖈𝖆𝖑 𝕰𝖓𝖈𝖗𝖞𝖕𝖙𝖎𝖔𝖓 𝕾𝖚𝖎𝖙𝖊"
    marquee_after_id = None
    marquee_speed_ms = 40
    marquee_dx = 2

    def stop_marquee():
        global marquee_after_id, title_canvas
        if marquee_after_id:
            try:
                root.after_cancel(marquee_after_id)
            except Exception:
                pass
            marquee_after_id = None
        if title_canvas:
            try:
                title_canvas.destroy()
            except Exception:
                pass
            title_canvas = None

    def start_marquee():
        global title_canvas, marquee_after_id
        stop_marquee()
        # Canvas inherits background to blend with header
        title_canvas = Canvas(title_area, height=36, highlightthickness=0)
        title_canvas.pack(fill=X, expand=1)
        # Create text starting at right edge and scroll left
        initial_x = title_canvas.winfo_width() or title_area.winfo_width() or 300
        text_id = title_canvas.create_text(initial_x, 18, text=TITLE_TEXT, anchor="w", font=("Segoe UI", 20, "bold italic"), fill="#0d6efd")

        def step():
            global marquee_after_id
            try:
                # Move left
                title_canvas.move(text_id, -marquee_dx, 0)
                bx = title_canvas.bbox(text_id)
                canvas_w = max(200, title_canvas.winfo_width())
                if bx and bx[2] < 0:
                    # Reset to right when fully off-screen
                    title_canvas.coords(text_id, canvas_w, 18)
                marquee_after_id = root.after(marquee_speed_ms, step)
            except Exception:
                marquee_after_id = None

        def init_and_go(_=None):
            global marquee_after_id
            try:
                title_canvas.delete("all")
                canvas_w = max(200, title_canvas.winfo_width())
                title_canvas.create_text(canvas_w, 18, text=TITLE_TEXT, anchor="w", font=("Segoe UI", 20, "bold italic"), fill="#0d6efd")
                marquee_after_id = root.after(marquee_speed_ms, step)
            except Exception:
                pass

        title_canvas.bind("<Configure>", init_and_go)

    def show_static_title():
        global title_lbl
        stop_marquee()
        if title_lbl is None:
            title_lbl = tb.Label(title_area, text=TITLE_TEXT, font=("Segoe UI", 22, "bold italic"), foreground="#0d6efd")
            title_lbl.pack(anchor="w", fill=X)

    def update_title_presentation():
        # Enable marquee when window is narrow; static when wide
        w = max(0, root.winfo_width())
        if w and w < 900:
            if title_lbl:
                try:
                    title_lbl.destroy()
                except Exception:
                    pass
            start_marquee()
        else:
            show_static_title()

    # Initialize title state
    update_title_presentation()

    banner_candidates = [
        os.path.join(BASE_DIR, "Classical Encryption Suite Banner Gothic Font.png"),
        os.path.join(BASE_DIR, "banner.png"),
        os.path.join(BASE_DIR, "header.png"),
    ]
    banner_path = next((p for p in banner_candidates if os.path.exists(p)), None)

    banner_orig = None
    if banner_path:
        banner_orig = Image.open(banner_path)

    def render_banner():
        try:
            if not banner_orig:
                banner_label.config(image='', text='')
                banner_label.image = None
                return
            # Enhanced scaling for a bolder, more appealing banner
            # Up to ~50% of window width, cap at 820px wide, target height ~150px
            avail_w = max(360, int(root.winfo_width() * 0.50))
            max_w = min(avail_w, 820)
            target_h = 150
            w, h = banner_orig.size
            if h <= 0 or w <= 0:
                return
            scale = min(max_w / w, target_h / h)
            new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
            img = banner_orig.resize((new_w, new_h), RESAMPLE)
            # Optional rounded corners for visual polish
            try:
                from PIL import ImageDraw
                radius = max(8, min(24, new_h // 6))
                mask = Image.new('L', (new_w, new_h), 0)
                draw = ImageDraw.Draw(mask)
                draw.rounded_rectangle((0, 0, new_w, new_h), radius=radius, fill=255)
                img.putalpha(mask)
            except Exception:
                pass
            photo = ImageTk.PhotoImage(img)
            banner_label.configure(image=photo)
            banner_label.image = photo
        except Exception as e:
            print("Banner render error:", e)

    render_banner()
    tb.Separator(root, orient="horizontal").pack(fill=X, padx=8, pady=(4,0))

    def _on_root_resize(event):
        render_banner()
        update_title_presentation()
    root.bind("<Configure>", _on_root_resize)
except Exception as e:
    print("Banner not loaded:", e)

# Split layout: left main content + right reference panel
main_pane = ttk.Panedwindow(root, orient="horizontal")
left_container = tb.Frame(main_pane)
right_container = tb.Frame(main_pane, padding=8)

# Tabs in left container
tabControl = ttk.Notebook(left_container)
decrypt_tab = tb.Frame(tabControl, padding=10)
encrypt_tab = tb.Frame(tabControl, padding=10)
tabControl.add(decrypt_tab, text="🔓 Decrypt")
tabControl.add(encrypt_tab, text="🔒 Encrypt")
tabControl.pack(expand=1, fill=BOTH, padx=5, pady=5)

# Reference panel in right container
ref_frame = tb.Labelframe(right_container, text="Cipher Reference", bootstyle=INFO)
ref_frame.pack(expand=1, fill=BOTH)
ref_text = tb.Text(ref_frame, wrap="word", height=10, width=36, font=("Segoe UI", 9), background="#f8fafc", borderwidth=2, relief="groove")
ref_text.pack(expand=1, fill=BOTH, padx=6, pady=6)
ref_content = (
    "Caesar: Shift letters by a fixed number.\n\n"
    "ROT13: Caesar with shift 13 (self-inverse).\n\n"
    "Atbash: Mirror substitution (A<->Z, B<->Y).\n\n"
    "Vigenere: Polyalphabetic with keyword-driven shifts.\n\n"
    "Playfair: 5x5 digraph substitution (I/J combined).\n\n"
    "Rail Fence: Zig-zag transposition across rails.\n\n"
    "Columnar: Column-based transposition keyed by word.\n\n"
    "Hill: Matrix-based polygraphic substitution.\n\n"
    "Bacon: 5-bit binary encoding of letters.\n\n"
    "Polybius: Coordinate pairs from 5x5 grid (I/J).\n\n"
    "Morse: Dots and dashes for letters/numbers.\n\n"
    "Scytale: Transposition with cylindrical wrap.\n"
)
ref_text.insert(END, ref_content)
ref_text.config(state=DISABLED)

# Add containers to pane and pack
main_pane.add(left_container, weight=3)
main_pane.add(right_container, weight=2)
main_pane.pack(expand=1, fill=BOTH, padx=5, pady=5)

# ---------- Decrypt Tab ----------
tb.Label(decrypt_tab, text="Decrypt Message", font=("Segoe UI", 14, "bold"), bootstyle=PRIMARY).pack(pady=(0,6))
decrypt_input = tb.Entry(decrypt_tab, width=60, font=("Segoe UI", 10))
decrypt_input.pack(padx=5, pady=5)
# Input toolbar for quick actions
decrypt_input_tools = tb.Frame(decrypt_tab)
decrypt_input_tools.pack(pady=(0,6))
_tb_btn_paste_dec = tb.Button(decrypt_input_tools, text="Paste", bootstyle=SECONDARY, width=10,
                              command=lambda: paste_into(decrypt_input))
_tb_btn_paste_dec.pack(side=LEFT, padx=4)
_tb_btn_clearin_dec = tb.Button(decrypt_input_tools, text="Clear", bootstyle=SECONDARY, width=10,
                                command=lambda: decrypt_input.delete(0, END))
_tb_btn_clearin_dec.pack(side=LEFT, padx=4)

decrypt_mode = tb.StringVar(value="Auto")
mode_frame = tb.Frame(decrypt_tab)
mode_frame.pack(pady=3)
tb.Radiobutton(mode_frame, text="Auto", variable=decrypt_mode, value="Auto", bootstyle=SUCCESS).pack(side=LEFT, padx=6)
tb.Radiobutton(mode_frame, text="Manual", variable=decrypt_mode, value="Manual", bootstyle=WARNING).pack(side=LEFT, padx=6)

cipher_var = tb.StringVar(value="Caesar")
cipher_menu = ttk.Combobox(decrypt_tab, textvariable=cipher_var, state="readonly",
                           values=[
                               "Caesar", "ROT13", "Atbash", "Vigenere", "Affine", "Rail Fence", "Columnar",
                               "Playfair", "Hill", "Bacon", "Polybius", "Morse", "Scytale", "Frequency Analysis"
                           ], font=("Segoe UI", 10))
cipher_menu.pack(padx=5, pady=3)

# --- Output box visually appealing and smaller ---
output_frame = tb.Labelframe(decrypt_tab, text="Decryption Output", bootstyle=INFO)
output_frame.pack(fill=None, padx=10, pady=8)
decrypt_output = tb.Text(output_frame, height=6, width=60, wrap="word", font=("Consolas", 10), background="#f8fafc", borderwidth=2, relief="groove")
decrypt_output.pack(padx=8, pady=8)
# Helper actions for outputs
def copy_text(widget):
    try:
        text = widget.get("1.0", END).strip()
        if text:
            root.clipboard_clear()
            root.clipboard_append(text)
    except Exception as _e:
        pass

def clear_text(widget):
    try:
        widget.config(state=NORMAL)
        widget.delete("1.0", END)
        widget.config(state=DISABLED)
    except Exception as _e:
        pass

# Safe paste helper for Entry widgets

def paste_into(entry_widget):
    try:
        txt = root.clipboard_get()
    except Exception:
        txt = ""
    entry_widget.delete(0, END)
    entry_widget.insert(0, txt)

# Output toolbar
decrypt_output_tools = tb.Frame(output_frame)
decrypt_output_tools.pack(pady=(0,4))
_tb_btn_copy_dec = tb.Button(decrypt_output_tools, text="Copy Output", bootstyle=INFO, width=14,
                             command=lambda: copy_text(decrypt_output))
_tb_btn_copy_dec.pack(side=LEFT, padx=4)
_tb_btn_clearout_dec = tb.Button(decrypt_output_tools, text="Clear Output", bootstyle=SECONDARY, width=14,
                                 command=lambda: clear_text(decrypt_output))
_tb_btn_clearout_dec.pack(side=LEFT, padx=4)

def decrypt_action():
    text = decrypt_input.get()
    if not text: return
    decrypt_output.config(state=NORMAL)
    decrypt_output.delete(1.0,END)
    cipher = cipher_var.get()
    mode = decrypt_mode.get()
    result = ""
    if cipher == "Caesar":
        if mode == "Auto":
            result = caesar_bruteforce(text)
        else:
            shift = simpledialog.askinteger("Caesar Key", "Enter shift:")
            result = caesar_encrypt(text, -shift) if shift is not None else "No shift entered."
    elif cipher == "ROT13":
        result = rot13(text)
    elif cipher == "Atbash":
        result = atbash(text)
    elif cipher == "Vigenere":
        key = simpledialog.askstring("Vigenere Key", "Enter key:")
        result = vigenere_decrypt(text, key) if key else "No key entered."
    elif cipher == "Affine":
        a = simpledialog.askinteger("Affine Key", "Enter a:")
        b = simpledialog.askinteger("Affine Key", "Enter b:")
        result = affine_decrypt(text, a, b) if a and b else "Affine keys missing."
    elif cipher == "Rail Fence":
        rails = simpledialog.askinteger("Rails", "Enter number of rails:")
        result = rail_fence_decrypt(text, rails) if rails else "No rails entered."
    elif cipher == "Columnar":
        key = simpledialog.askstring("Columnar Key", "Enter key:")
        result = columnar_decrypt(text, key) if key else "No key entered."
    elif cipher == "Playfair":
        key = simpledialog.askstring("Playfair Key", "Enter key (letters):")
        result = playfair_decrypt(text, key) if key else "No key entered."
    elif cipher == "Hill":
        size = simpledialog.askinteger("Hill Size", "Enter matrix size (2 or 3):")
        if size in [2,3]:
            key = []
            for i in range(size):
                row = simpledialog.askstring("Hill Key", f"Row {i+1} (letters):")
                if not row or len(row)!=size: result="Invalid key"; break
                key.append(row.lower())
            else:
                result = hill_decrypt(text, key)
        else:
            result = "Invalid matrix size."
    elif cipher == "Bacon":
        result = bacon_decrypt(text)
    elif cipher == "Polybius":
        result = polybius_decrypt(text)
    elif cipher == "Morse":
        result = morse_decrypt(text)
    elif cipher == "Scytale":
        diameter = simpledialog.askinteger("Scytale", "Enter diameter:")
        result = scytale_decrypt(text, diameter) if diameter else "No diameter entered."
    elif cipher == "Frequency Analysis":
        result = freq_analysis(text)
    decrypt_output.insert(END, result)
    decrypt_output.config(state=DISABLED)

# --- Decrypt button just below output box ---
cta_dec = tb.Frame(decrypt_tab)
cta_dec.pack(pady=6)
decrypt_btn = tb.Button(cta_dec, text="🔓 Decrypt", bootstyle="INFO-outline", command=decrypt_action, width=18)
decrypt_btn.pack()
stylize_cta_button(decrypt_btn, "INFO-outline", "INFO")

# ---------- Guide (compact, visually appealing at bottom) ----------
guide_frame = tb.Labelframe(root, text="", bootstyle=INFO)
guide_frame.pack(side=BOTTOM, fill=X, padx=12, pady=6)

# Title (bold, blue, inline)
title_label = tb.Label(
    guide_frame,
    text="Nitz's Ultimate Crypto Cipher Tool",
    font=("Segoe UI", 11, "bold"),
    foreground="#0078D7",
    anchor="w",
    justify=LEFT
)
title_label.pack(fill=X, padx=8, pady=(2,0))

# Divider line
divider = tb.Separator(guide_frame, orient="horizontal")
divider.pack(fill=X, padx=8, pady=(0,4))

# Compact vertical features layout
features = [
    "• Encrypt and decrypt classical ciphers: Caesar, ROT13, Atbash, Vigenere, Affine, Rail Fence, Columnar, Playfair, Hill, Bacon, Polybius, Morse, Scytale.",
    "• Use the Encrypt/Decrypt tabs. Enter key when prompted.",
    "• Outputs only correct decryption. Beginner-friendly and fully functional.",
    "• Tip: For guaranteed results, switch to Manual mode and enter the correct shift value—this ensures 100% accuracy for any input!"
]

for f in features:
    tb.Label(
        guide_frame,
        text=f,
        font=("Segoe UI", 9),
        anchor="w",
        justify=LEFT,
        wraplength=1200,
        foreground="#0078D7" if "Tip:" in f else None
    ).pack(fill=X, padx=16, pady=0)

# ---------- Encrypt Tab ----------
tb.Label(encrypt_tab, text="Encrypt Message", font=("Segoe UI", 14, "bold"), bootstyle=SUCCESS).pack(pady=(0,6))
encrypt_input = tb.Entry(encrypt_tab, width=60, font=("Segoe UI", 10))
encrypt_input.pack(padx=5, pady=5)
# Input toolbar for quick actions
encrypt_input_tools = tb.Frame(encrypt_tab)
encrypt_input_tools.pack(pady=(0,6))
_tb_btn_paste_enc = tb.Button(encrypt_input_tools, text="Paste", bootstyle=SECONDARY, width=10,
                              command=lambda: paste_into(encrypt_input))
_tb_btn_paste_enc.pack(side=LEFT, padx=4)
_tb_btn_clearin_enc = tb.Button(encrypt_input_tools, text="Clear", bootstyle=SECONDARY, width=10,
                                command=lambda: encrypt_input.delete(0, END))
_tb_btn_clearin_enc.pack(side=LEFT, padx=4)

encrypt_cipher_var = tb.StringVar(value="Caesar")
encrypt_menu = ttk.Combobox(encrypt_tab, textvariable=encrypt_cipher_var, state="readonly",
                            values=[
                                "Caesar", "ROT13", "Atbash", "Vigenere", "Affine", "Rail Fence", "Columnar",
                                "Playfair", "Hill", "Bacon", "Polybius", "Morse", "Scytale"
                            ], font=("Segoe UI", 10))
encrypt_menu.pack(padx=5, pady=3)

encrypt_output_frame = tb.Labelframe(encrypt_tab, text="Encryption Output", bootstyle=SUCCESS)
encrypt_output_frame.pack(fill=None, padx=10, pady=8)
encrypt_output = tb.Text(encrypt_output_frame, height=6, width=60, wrap="word", font=("Consolas", 10), background="#f8fafc", borderwidth=2, relief="groove")
encrypt_output.pack(padx=8, pady=8)
# Output toolbar
encrypt_output_tools = tb.Frame(encrypt_output_frame)
encrypt_output_tools.pack(pady=(0,4))
_tb_btn_copy_enc = tb.Button(encrypt_output_tools, text="Copy Output", bootstyle=SUCCESS, width=14,
                             command=lambda: copy_text(encrypt_output))
_tb_btn_copy_enc.pack(side=LEFT, padx=4)
_tb_btn_clearout_enc = tb.Button(encrypt_output_tools, text="Clear Output", bootstyle=SECONDARY, width=14,
                                 command=lambda: clear_text(encrypt_output))
_tb_btn_clearout_enc.pack(side=LEFT, padx=4)

def encrypt_action():
    text = encrypt_input.get()
    if not text: return
    encrypt_output.config(state=NORMAL)
    encrypt_output.delete(1.0,END)
    cipher=encrypt_cipher_var.get()
    result=""
    if cipher=="Caesar":
        shift=simpledialog.askinteger("Caesar Key","Enter shift:")
        result=caesar_encrypt(text,shift) if shift is not None else "No shift entered."
    elif cipher=="ROT13":
        result=rot13(text)
    elif cipher=="Atbash":
        result=atbash(text)
    elif cipher=="Vigenere":
        key=simpledialog.askstring("Vigenere Key","Enter key:")
        result=vigenere_encrypt(text,key) if key else "No key entered."
    elif cipher=="Affine":
        a=simpledialog.askinteger("Affine Key","Enter a:")
        b=simpledialog.askinteger("Affine Key","Enter b:")
        result=affine_encrypt(text,a,b) if a and b else "Affine keys missing."
    elif cipher=="Rail Fence":
        rails=simpledialog.askinteger("Rails","Enter number of rails:")
        result=rail_fence_encrypt(text,rails) if rails else "No rails entered."
    elif cipher=="Columnar":
        key=simpledialog.askstring("Columnar Key","Enter key:")
        result=columnar_encrypt(text,key) if key else "No key entered."
    elif cipher=="Playfair":
        key = simpledialog.askstring("Playfair Key", "Enter key (letters):")
        result = playfair_encrypt(text, key) if key else "No key entered."
    elif cipher=="Hill":
        size = simpledialog.askinteger("Hill Size", "Enter matrix size (2 or 3):")
        if size in [2,3]:
            key = []
            for i in range(size):
                row = simpledialog.askstring("Hill Key", f"Row {i+1} (letters):")
                if not row or len(row)!=size: result="Invalid key"; break
                key.append(row.lower())
            else:
                result = hill_encrypt(text, key)
        else:
            result = "Invalid matrix size."
    elif cipher=="Bacon":
        result = bacon_encrypt(text)
    elif cipher=="Polybius":
        result = polybius_encrypt(text)
    elif cipher=="Morse":
        result = morse_encrypt(text)
    elif cipher=="Scytale":
        diameter = simpledialog.askinteger("Scytale", "Enter diameter:")
        result = scytale_encrypt(text, diameter) if diameter else "No diameter entered."
    encrypt_output.insert(END,result)
    encrypt_output.config(state=DISABLED)

cta_enc = tb.Frame(encrypt_tab)
cta_enc.pack(pady=6)
encrypt_btn = tb.Button(cta_enc, text="🔒 Encrypt", bootstyle="SUCCESS-outline", command=encrypt_action, width=18)
encrypt_btn.pack()
stylize_cta_button(encrypt_btn, "SUCCESS-outline", "SUCCESS")

# ---------- Connect / Socials (polished) ----------
connect_frame = tb.Labelframe(root, text="Connect", bootstyle=INFO)
connect_frame.pack(pady=8, padx=8, fill=X)
links_row = tb.Frame(connect_frame)
links_row.pack(padx=8, pady=6, fill=X)

# Load icons (update paths if needed)
try:
    insta_path = os.path.join(BASE_DIR, "Instagram_icon.png")
    linkedin_path = os.path.join(BASE_DIR, "LinkedIn_logo_initials.png")
    mail_path = os.path.join(BASE_DIR, "Mail_(iOS).png")

    insta_icon = ImageTk.PhotoImage(Image.open(insta_path).resize((22,22), RESAMPLE)) if os.path.exists(insta_path) else None
    linkedin_icon = ImageTk.PhotoImage(Image.open(linkedin_path).resize((22,22), RESAMPLE)) if os.path.exists(linkedin_path) else None
    mail_icon = ImageTk.PhotoImage(Image.open(mail_path).resize((22,22), RESAMPLE)) if os.path.exists(mail_path) else None
except Exception as e:
    insta_icon = linkedin_icon = mail_icon = None
    print("Social icons not loaded:", e)

def open_url(url):
    webbrowser.open(url)

# Professional link-style buttons (optionally with icons)

def link(text, url, image=None):
    btn = tb.Button(
        links_row,
        text=text,
        bootstyle=LINK,
        cursor="hand2",
        image=image,
        compound=LEFT,
        command=lambda: open_url(url)
    )
    if image:
        btn.image = image
    btn.pack(side=LEFT, padx=8)
    return btn

# Use icons if available; otherwise links render as clean text
link("Email", "mailto:niteshrajanagalu@gmail.com", mail_icon if 'mail_icon' in globals() and mail_icon else None)
link("🐞 Report bugs", "mailto:niteshrajanagalu@gmail.com?subject=Bug%20Report")
link("Instagram", "https://www.instagram.com/nitesh_ig/", insta_icon if 'insta_icon' in globals() and insta_icon else None)
link("LinkedIn", "https://www.linkedin.com/in/niteshrajanagalu/", linkedin_icon if 'linkedin_icon' in globals() and linkedin_icon else None)

# ---------- Copyright & Branding ----------
copyright_frame = tb.Frame(root)
copyright_frame.pack(side=BOTTOM, fill=X, padx=0, pady=0)

tb.Label(
    copyright_frame,
    text="© 2025 Nitz's Ultimate Crypto Cipher Tool — All Rights Reserved",
    font=("Segoe UI", 11, "bold italic"),
    foreground="#0078D7",
    anchor="center"
).pack(fill=X, pady=2)

# Live preview for select ciphers (as you type)

def live_set_output(widget, text):
    try:
        widget.config(state=NORMAL)
        widget.delete("1.0", END)
        widget.insert(END, text)
        widget.config(state=DISABLED)
    except Exception:
        pass

def update_live_preview_decrypt(event=None):
    try:
        text = decrypt_input.get()
        cipher = cipher_var.get()
        mode = decrypt_mode.get()
        res = None
        if cipher == "ROT13":
            res = rot13(text)
        elif cipher == "Atbash":
            res = atbash(text)
        elif cipher == "Frequency Analysis":
            res = freq_analysis(text) if text else ""
        elif cipher == "Caesar" and mode == "Auto":
            # Light preview, may be slower on long text
            res = caesar_bruteforce(text) if text else ""
        if res is not None:
            live_set_output(decrypt_output, res)
    except Exception:
        pass

def update_live_preview_encrypt(event=None):
    try:
        text = encrypt_input.get()
        cipher = encrypt_cipher_var.get()
        res = None
        if cipher == "ROT13":
            res = rot13(text)
        elif cipher == "Atbash":
            res = atbash(text)
        if res is not None:
            live_set_output(encrypt_output, res)
    except Exception:
        pass

# Bind live preview events
decrypt_input.bind("<KeyRelease>", update_live_preview_decrypt)
encrypt_input.bind("<KeyRelease>", update_live_preview_encrypt)
cipher_menu.bind("<<ComboboxSelected>>", update_live_preview_decrypt)
encrypt_menu.bind("<<ComboboxSelected>>", update_live_preview_encrypt)

# Keyboard shortcuts for productivity

def is_decrypt_active():
    try:
        return tabControl.index(tabControl.select()) == 0
    except Exception:
        return True

def trigger_primary_action(event=None):
    if is_decrypt_active():
        decrypt_action()
    else:
        encrypt_action()

def copy_current_output(event=None):
    if is_decrypt_active():
        copy_text(decrypt_output)
    else:
        copy_text(encrypt_output)

def clear_current_input(event=None):
    if is_decrypt_active():
        decrypt_input.delete(0, END)
    else:
        encrypt_input.delete(0, END)

root.bind_all("<Control-Return>", trigger_primary_action)
root.bind_all("<Control-Shift-Key-C>", copy_current_output)
root.bind_all("<Control-l>", clear_current_input)

root.mainloop()
