username=input("Please enter your Name: \n")  #ask the user his/her name and will use it throughout the program
print("Welcome to the modified Apple Museum",username)
print('''Here you will be able to see what Apple has come from and where Apple is now.
It has come from a statup founded by two people to a trillion dollar company.
The company was founded by Mr. Steve jobs, Mr. Ronald Wayneand Mr. Steve Wozniak. 
Apple motto was does more, costs less, its that simple ''')                      #brief history about apple and the names of the founder
while True:
    a=(input('''Please choose your choice by entering the number next to the topic that interests you:
    1.The Iphone               
    2.The Airpods
    3.The Apple watch 
    4.The Apple T.V
    5.The Apple Book
    #.Exit the museum\n''')) #list of the products made by apple
    if a=='1':                          #if 1 is entered it will enter the iphone menu
        print("Please choose your Iphone choice by entering the number next to the iphone. And if you want to exit the program, please enter '#'")
        print("1.Iphone 2g")
        print("2.Iphone 3g")
        print("3.Iphone 3gs")
        print("4.Iphone 4")
        print("5.Iphone 4s")
        print("6.Iphone 5")
        print("7.Iphone 5s")
        print("8.Iphone 5c")
        print("9.Iphone 6")
        print("10.Iphone 6s")
        print("11.Iphone 6 Plus")
        print("12.Iphone 6s Plus")
        print("13.Iphone 7")
        print("14.Iphone 7 Plus")
        print("15.Iphone 8 ")
        print("16.Iphone 8 PLus")
        print("17.Iphone X")
        print("18.Iphone Xs")
        print("19.Iphone Xs Max")
        print("20.Iphone XR")
        print("21.Iphone SE")
        print("22.Iphone SE 2020")
        print("23.Iphone 11")
        print("24.Iphone 11 Pro")
        print("25.Iphone 11 Pro Max")
        print("26.Iphone 12")
        print("27.Iphone 12 Pro")
        print("28.Iphone 12 Pro Max")
        print("29.Iphone 12 Pro Mini")
        print("30.Iphone 13")
        print("31.Iphone 13 Pro")
        print("32.Iphone 13 Pro Max")
        print("33.Iphone 13 Mini")
        print("#.Go to the previous menu")
        print("PLEASE NOTE THAT IF WE ARE TALKING ABOUT THE PRICE RANGE OF DISCONTINUED IPHONES, IT MAY NOT BE A 100% ACCURATE.")
        while True:
             #using while true so that we can keep looking at different iphones while using the program
            b=(input("please enter the number of the iphone you want to know about:\n"))
            if b=='#':
                break
            elif int(b)>33 or int(b)==0:
                print("Invalid Entry Please try Again")
                break
            elif int(b)==1:
                print('''
                The iphone 2G was the first iphone to be launched by Apple in 2007. 
                Weighing only 135g, it was different from the competitors present at that time. 
                It had a 412 mhz processor, with internal storage ranging from 4 to 16gb.
                It only had a back camera of 2mp but it could take really good photos.
                It could connect via wifi and Bluetooth. It only came in black colour. 
                Price range staring from 37,000 rs.''')
            elif int(b)==2:
                print('''
                The iphone 3G was announced in 2008.
                It weighed about 133g. it had the similar processor with 412 mhz.
                it had 128mb ram. And internal storage starting from 8gb to 16gb.
                It had the same camera specification. It introduced a gps in the phone.
                It came in two flavours black and white.''')
            elif int(b)==3:
                print('''
                The Iphone 3Gs was launched in 2009.
                It was the first iphone that could record videos at 30fps.
                With a better processor than the predecessor.
                It cam with a 600mhz processor and 256 mb ram.
                It also came in 2 colour styles black and white.''')
            elif int(b)==4:
                print('''
                The Iphone 4 was released in 2010.
                It had the first IPS LCD display type.
                With 1 ghz processor and 512mb ram and internal storage from 8gb to 32gb.
                It came with the first processor which was rated at 1ghz.
                It was also the first Iphone to have a front facing selfie camera. 
                It also came in two colours black and white.''')
            elif int(b)==5:
                print('''
                The Iphone 4s was released in 2011.
                It also came with a 1ghz processor but it was dual core.
                It was the first iphone which had internal storage capacity from 8gb to 64gb.
                It had 512mb ram.
                The back facing camera was rated 8mp
                and was capable of recording 1080p videos at 30fps.
                It also came in two flavours: black and white.''')
            elif int(b)==6:
                print('''
                The Iphone 5 was launched in 2012.
                The phone came with an 1.3 ghz dual core processor
                and a apple a6 chip(32nm). The phone came in different variants: 
                16gb storage and 1gb ram,
                32gb storage and 1 gb ram,
                64gb and 1gb ram.
                This phone had a front facing camera which was able to
                record at 720p at 30fps.''')
            elif int(b)==7:
                print('''
                The Iphone 5s was launched in 2013.
                It came with a similiar processor as Iphone 5
                but the difference was that it came with 
                a different chipset which was called Apple A7.
                It was the first iphone to get a biometric lock,
                namely the fingerprint scanner.
                The back camera was able to record videos at 720p resolution at 120fps.
                The phone came in three flavours:
                space grey
                white/silver
                and gold.''')
            elif int(b)==8:
                print('''
                The Iphone 5c was released in 2013.
                It was mostly an Iphone for kids.
                The phone came with an 1.3 ghz dual core processor
                and a apple a6 chip(32nm). The phone came in different variants: 
                16gb storage and 1gb ram,
                32gb storage and 1 gb ram,
                64gb and 1gb ram.
                This phone had a front facing camera which was able to
                record at 720p at 30fps.''')
            elif int(b)==9:
                print('''
                The Iphone 6 was released in 2014.
                It was the first Iphone that
                came with the feature named as Apple Pay.
                The phone came with an 1.4 ghz dual core processor
                and a apple a8 chip(20nm). The phone came in different variants: 
                16gb storage and 1gb ram,
                32gb storage and 1 gb ram,
                64gb and 1gb ram
                and lastly 128gb and 1gb ram.
                This phone had a back facing camera which was able to
                record at 1080p at 60fps and 720p at 240fps.
                it came in three flavours:
                silver
                space grey 
                gold''')
            elif int(b)==10:
                print('''
                The Iphone 6s was released in 2015.
                It was the first Iphone that
                came with the feature named as 3d touch.
                The phone came with an 1.84 ghz dual core processor
                and a apple a9 chip(14nm). The phone came in different variants: 
                16gb storage and 2gb ram,
                32gb storage and 2gb ram,
                64gb and 2gb ram
                and lastly 128gb and 2gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in three flavours:
                silver
                space grey 
                gold''')
            elif int(b)==11:
                print('''
                The Iphone 6 Plus was released in 2014.
                It was the first Iphone that
                came with the in a bigger size than its main branch.
                The phone came with an 1.4 ghz dual core processor
                and a apple a8 chip(20nm). The phone came in different variants: 
                16gb storage and 1gb ram,
                32gb storage and 1 gb ram,
                64gb and 1gb ram
                and lastly 128gb and 1gb ram.
                This phone had a back facing camera which was able to
                record at 1080p at 60fps and 720p at 240fps.
                it came in three flavours:
                silver
                space grey 
                gold''')
            elif int(b)==12:
                print('''
                The Iphone 6s plus was released in 2015.
                The phone came with an 1.84 ghz dual core processor
                and a apple a9 chip(14nm). The phone came in different variants: 
                16gb storage and 2gb ram,
                32gb storage and 2gb ram,
                64gb and 2gb ram
                and lastly 128gb and 2gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in four flavours:
                silver
                space grey 
                gold
                rose gold''')
            elif int(b)==13:
                print('''
                The Iphone 7 was released in 2016.
                The phone came with an 2.34 ghz quad core processor
                and a apple a10 fusion chip(16nm). The phone came in different variants: 
                32gb storage and 2gb ram,
                64gb and 2gb ram,
                128gb and 2gb ram
                and lastly 256gb and 2gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in four flavours:
                jet black,
                black(matte)
                silver,
                gold,
                rose gold,
                red''')
            elif int(b)==14:
                print('''
                The Iphone 7 Plus was released in 2016.
                The phone came with an 2.34 ghz quad core processor
                and a apple a10 fusion chip(16nm). The phone came in different variants: 
                32gb storage and 3gb ram,
                64gb and 3gb ram,
                128gb and 3gb ram
                and lastly 256gb and 3gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in four flavours:
                jet black,
                black(matte)
                silver,
                gold,
                rose gold,
                red''')
            elif int(b)==15:
                print('''
                The Iphone 8 was released in 2017.
                The phone came with an hexa core processor
                and a apple a11 bionic chip(10nm). The phone came in different variants: 
                64gb and 2gb ram,
                128gb and 2gb ram
                and lastly 256gb and 2gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in four flavours:
                silver,
                gold,
                space grey,
                red''')
            elif int(b)==16:
                print('''
                The Iphone 8 plus was released in 2017.
                The phone came with an hexa core processor
                and a apple a11 bionic chip(10nm). The phone came in different variants: 
                64gb and 3gb ram,
                128gb and 3gb ram
                and lastly 256gb and 3gb ram.
                This phone had a back facing camera which was able to
                record at 4k resolution at 30fps.
                it came in four flavours:
                silver,
                gold,
                space grey,
                red''')
            elif int(b)==17:
                print('''
                The Iphone X/10 was released in 2017.
                The phone came with an 2.39 ghz hexa core processor
                and a apple a11 bionic chip(10nm). The phone came in different variants: 
                64gb and 3gb ram,
                256gb and 3gb ram.
                it came in 2 flavours:
                space grey
                silver''')
            elif int(b)==18:
                print('''
                The Iphone Xs was released in 2018.
                The phone came in different variants: 
                64 gb and 4gb ram,
                256 gb and 4gb ram
                512 gb and 4gb ram.
                it came with a dual camera set up with both cameras rated at 12 mp.
                it came in 3 flavours:
                space grey
                silver
                gold''')
            elif int(b)==19:
                print('''
                The Iphone Xs max  was released in 2018.
                The phone came in different variants: 
                64 gb and 4gb ram,
                256 gb and 4gb ram
                512 gb and 4gb ram.
                it came with a dual camera set up with both cameras rated at 12 mp.
                it came in 3 flavours:
                space grey
                silver
                gold''')
            elif int(b)==20:
                print('''
                The Iphone XR  was released in 2018.
                The phone came in different variants: 
                64 gb and 3gb ram,
                128 gb and 3gb ram
                256 gb and 3gb ram.
                it came with a dual camera set up with both cameras rated at 12 mp.
                it came in different flavours:
                black,
                red,
                yellow,
                blue,
                coral,
                white.
                The price starts from 43,000rs''')
            elif int(b)==21:
                print('''
                The Iphone SE was launched in 2016.
                The phone was just like the Iphone 6s but in the casing of an iphone 5
                It came with a dual core 1.84 Ghz and a 6 core graphics processor.
                It came in different variants:
                16 GB AND 2GB RAM,
                32GB AND 2GB RAM,
                64GB AND 2GB RAM,
                128GB AND 2GB RAM.
                It came in different flavours:
                Space Gray,
                Silver,
                Gold
                Rose gold.
                ''')
            elif int(b)==22:
             print('''
                The Iphone SE v2 was launched in 2020.
                It came with a hexa core and a 4 core graphics processor.
                It came in different variants:
                64 GB AND 3GB RAM,
                128GB AND 3GB RAM,
                256GB AND 3GB RAM.
                It came in different flavours:
                black,
                white,
                red.
                ''')
            elif int(b)==23:
                print('''
                The Iphone 11  was released in 2019.
                The phone came in different variants: 
                64 gb and 4gb ram,
                128 gb and 4gb ram,
                256 gb and 4gb ram.            
                it came with a dual camera set up with both cameras rated at 12 mp.
                it came in several flavours:
                Black,
                Green,
                yellow,
                Purple,
                Red, 
                White''')
            elif int(b)==24:
                print('''
                The Iphone 11 pro  was released in 2019.
                The phone came in different variants: 
                64 gb and 4gb ram,
                256 gb and 4gb ram,
                512 gb and 4gb ram.            
                it came with a triple camera set up with all three cameras rated at 12 mp.
                it came in several flavours:
                Matte Space Gray,
                Matte Silver,
                Matte Gold,
                Matte Midnight Green''')
            elif int(b)==25:
                print('''
                The Iphone 11 Pro Max  was released in 2019.
                The phone came in different variants: 
                64 gb and 4gb ram,
                256 gb and 4gb ram,
                512 gb and 4gb ram.            
                it came with a triple camera set up with all three cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                Matte Space Gray,
                Matte Silver,
                Matte Gold,
                Matte Midnight Green''')
            elif int(b)==26:
                print('''The Iphone 12  was released in 2020.
                The phone came in different variants: 
                64 gb and 4gb ram,
                128gb and 4gb ram,
                256 gb and 4gb ram.            
                it came with a dual camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                black,
                white,
                red,
                green,
                blue,
                purple.''')
            elif int(b)==27:
                print('''The Iphone 12 Pro was released in 2020.
                The phone came in different variants: 
                128gb and 6gb ram,
                256 gb and 6gb ram,
                512 gb and 6gb ram.            
                it came with a triple camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                silver,
                graphite,
                gold,
                pacific blue.''')
            elif int(b)==28:
                print('''The Iphone 12 Pro Max was released in 2020.
                The phone came in different variants: 
                128gb and 6gb ram,
                256 gb and 6gb ram,
                512 gb and 6gb ram.            
                it came with a triple camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                silver,
                graphite,
                gold,
                pacific blue.''')
            elif int(b)==29:
                print('''The Iphone 12 Pro Mini was released in 2020.
                The phone came in different variants: 
                64 gb and 4gb ram,
                128gb and 4gb ram,
                256 gb and 4gb ram.            
                it came with a dual camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                black,
                white,
                red,
                green,
                blue,
                purple.''')
            elif int(b)==30:
                print('''The Iphone 13 was released in 2021.
                The phone came in different variants: 
                128gb and 4gb ram,
                256 gb and 4gb ram,
                512 gb and 4gb ram.            
                it came with a dual camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                starlight,
                midnight,
                red,
                blue,
                pink.''')
            elif int(b)==31:
                print('''The Iphone 13 Pro was released in 2021.
                The phone came in different variants: 
                128gb and 6gb ram,
                256 gb and 6gb ram,
                512 gb and 6gb ram
                1tb and 6gb ram.            
                it came with a Quad camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                silver,
                graphite,
                gold,
                sierra blue.''')
            elif int(b)==32:
                print('''The Iphone 13 Pro max was released in 2021.
                The phone came in different variants: 
                128gb and 6gb ram,
                256 gb and 6gb ram,
                512 gb and 6gb ram
                1tb and 6gb ram.            
                it came with a Quad camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                silver,
                graphite,
                gold,
                sierra blue.''')
            elif int(b)==33:
                print('''The Iphone 13 Mini was released in 2021.
                The phone came in different variants: 
                128gb and 4gb ram,
                256 gb and 4gb ram,
                512 gb and 4gb ram.            
                it came with a dual camera set up with all cameras rated at 12 mp.
                it also came with a dual camera selfie setup.
                it came in several flavours:
                starlight,
                midnight,
                blue,
                pink,
                red.''')
            else:
                print( "You entered an invalid Entry. Please try again.")
    elif a=='2':
        print('''
    AirPods are wireless Bluetooth earbuds designed by Apple. 
    They were first announced on September 7, 2016, with a second generation announced and released in March 2019. 
    They are Apple's entry-level wireless headphones, sold alongside the AirPods Pro and AirPods Max. 
    Within two years, they became Apple's most popular accessory.''')
        print('''
    
    
    Please enter the number of menu corresponding to the name of the model of airpods.''')
        print("1.Apple AirPods (1st Gen)")
        print("2.Apple AirPods (2nd Gen)")
        print("3.AirPods Pro")
        print("4.Airpods Pro Max")
        print("*.Go to the previous menu")
        d=input("Please enter the number corresponding to the model of the airpod you want to know about\n")
    
        if d=='*':
            exit
        elif int(d)==1:
            print('''
            Driven by the custom Apple W1 chip, AirPods use optical sensors and a motion accelerometer to detect when they’re in your ears.
            Whether you’re using both AirPods or just one, the W1 chip automatically routes the audio and engages the microphone. 
            And when you’re on a call or talking to Siri, an additional accelerometer works with beamforming microphones to filter out background noise and focus on the sound of your voice. 
            Because the ultralow-power W1 chip manages battery life so well, AirPods deliver an incredible 5 hours of listening time on one charge.2 And they’re made to keep up with you, 
            thanks to a charging case that holds multiple additional charges for more than 24 hours of listening time.3 Need a quick charge? Just 15 minutes in the case gives you 3 hours of listening time.
            ''')
        elif int(d)==2:
            print('''
            With more talk time, voice-activated Siri access — and a wireless charging case- AirPods deliver an unparalleled wireless headphone experience.
            Simply take them out and they’re ready to use with all your devices. 
            Put them in your ears and they connect immediately, immersing you in rich, high-quality sound. 
            Just like magic.''')
        elif int(d)==3:
            print('''
            AirPods Pro are the only in-ear headphones with Active Noise Cancellation that continuously adapts to the geometry of your ear and the fit of the ear tips — blocking out the world 
            so you can focus on what you’re listening to. An outward-facing microphone detects external sound.
            AirPods Pro then counter it with equal anti-noise, cancelling the external sound before you hear it''')
        elif int(d)==4:
            print('''
            The over-ear headphone has been completely reimagined. 
            From cushion to canopy, AirPods Max are designed for an uncompromising fit that creates the optimal acoustic seal for many different head shapes — fully immersing you in every sound.
            AirPods Max combine high-fidelity audio with industry-leading Active Noise Cancellation to deliver an unparalleled listening experience. 
            Each part of their custom-built driver works to produce sound with ultra-low distortion across the audible range. 
            From deep, rich bass to accurate mids and crisp, clean highs, you’ll hear every note with a new sense of clarity.''')
        else:
            print("You entered an invalid Entry. Please try again.")
        
    elif a=='3':
        print('''
    Apple Watch is a line of smartwatches produced by Apple Inc.
    It incorporates fitness tracking, health-oriented capabilities, 
    and wireless telecommunication, and integrates with iOS and other Apple products and services.
    The Apple Watch was released in April 2015 and quickly became the best-selling wearable device: 4.2 million were sold in the second quarter of fiscal 2015,and more than 100 million people were estimated to use an Apple Watch as of December 2020.
    Apple has introduced new generations of the Apple Watch with improved internal components each September—each labeled by Apple a 'Series', with certain exceptions.
   

    Each Series has been initially sold in multiple variants defined by the watch casing's material, color, and size (except for the budget watches Series 1 and SE, available only in aluminum), and beginning with Series 3, by the option in the aluminum variants for LTE cellular connectivity, which comes standard with the other materials.[30] The band included with the watch can be selected from multiple options from Apple, and watch variants in aluminum co-branded with Nike and in stainless steel co-branded with Hermès are also offered, which include exclusive bands and digital watch faces carrying those companies' brandings.


    The Apple Watch operates primarily in conjunction with the user's iPhone for functions such as configuring the watch and syncing data with iPhone apps, but can separately connect to a Wi-Fi network for some data-reliant purposes, including basic communications and audio streaming.
    LTE-equipped models can independently connect to a mobile network, including for calling, texting, and installed mobile app data use, substantially reducing the need for an iPhone after initial setup.
    The oldest iPhone model that is compatible with any given Apple Watch depends on the version of system software installed on each device. As of September 2021, new Apple Watches come with watchOS 8 preinstalled and require an iPhone running iOS 15, which is available for the iPhone 6S and later.''')
    
    elif a=='4':
        print('''Apple TV is a digital media player and microconsole developed and sold by Apple Inc.
    It is a small network appliance and entertainment device that can receive digital data for visual and audio content such as music, video,
    video games, or the screen display of certain other devices, and play it on a connected television set or other video display.
    Apple TV is an HDMI-compliant source device.
    To use it for viewing, it has to be connected to an enhanced-definition or high-definition widescreen television via an HDMI cable.
    The device has no integrated controls and can only be controlled remotely,
    either by an Apple Remote or Siri Remote control device (which is included with Apple TV) using its infrared/Bluetooth capability,
    by the Apple TV Remote app (downloadable from App Store) on numerous Apple devices using its Wi-Fi capability,
    or by some third-party gaming controllers and infrared remotes.''')
        print('''
    The different Apple Tv models launched by Apple are :
    1)Apple tv generation 1
    2)Apple tv generation 2
    3)3rd generation
    4)HD (previously 4th generation)
    5)4K (1st generation)
    6)4K (2nd generation)
    *)Go to the previous menu.''')
        while True:
            f=(input("please enter the number corresponding to the model of the apple tv you want know about"))
            if str(f)=='*':
                break
            elif int(f)==1:
                print('''
    Apple TV generation 1 runs software applications preinstalled with the system software or,
    for models running tvOS, downloaded from Apple's tvOS App Store over the device's Wi-Fi connection, 
    with the most popular being those that stream video.
    Major online content sources for Apple TV apps include subscription services for streaming television and film, 
    cable and broadcast networks via TV Everywhere, and major sports leagues.
    Its Wi-Fi capability is also used to receive content purchased or rented directly from Apple's iTunes Store, 
    transmitted from other nearby iDevices via AirPlay, or shared from macOS or Windows computers running iTunes.''')
            elif int(f)==2:
                print('''
    The 2nd generation Apple TV was announced on September 1, 2010, 
    and was the first to run on a variant of iOS. The device is housed in a smaller, 
    all-black case, one-quarter the size of the original. 
    This model replaced the internal hard drive with 8 GB internal flash storage, 
    enough local storage for buffering purposes; all media became streamed, 
    instead of synced. It supports output up to 720p over HDMI only.''')
            elif int(f)==3:
                print('''
    On March 7, 2012, Apple announced the 3rd generation Apple TV (model A1427) at an Apple Special Event. 
    It is identical externally to the second generation model, includes a dual-core A5 processor with one core 
    deactivated or unused,[46] and supports 1080p output.Apple silently released a third generation "Rev A" 
    (model A1469) on January 28, 2013 with component changes included. This refreshed model gained support 
    for peer to peer Airplay which allowed iOS devices to mirror to the Apple TV without requiring both devices 
    to be on the same Wi-Fi network.''')
            elif int(f)==4:
                print('''
            On September 9, 2015, Apple announced the fourth-generation Apple TV at an Apple Special Event. 
            The fourth-generation model uses a new operating system, tvOS, with an app store, 
            allowing downloads of third-party apps for video, audio, games and other content. 
            Upon release, third-party apps were available from a limited range of providers, 
            with new APIs providing opportunities for more apps. A requirement of new apps and 
            games was that they must include interfacing with the new touchpad-enabled Siri remote, 
            which was later relaxed for games. In March 2019 Apple rebranded the device as Apple TV HD.''')
            elif int(f)==5:
                print('''
    At an Apple Special Event on September 12, 2017, Apple announced the Apple TV 4K which supports 2160p output, 
    HDR10, Dolby Vision, and includes a faster Apple A10X Fusion processor supporting HEVC hardware decoding. 
    Dolby Atmos support was added in tvOS 12.Following the announcement of the new models, the 64 GB version 
    of the Apple TV HD was discontinued.Externally it is similar to the 4th generation model, with the only 
    differences being the addition of vents on the base, the removal of the USB-C port, and the addition of a 
    tactile white ring around the Menu button on the included Siri Remote.''')
            elif int(f)==6:
                print('''
    On April 20, 2021, Apple announced an updated Apple TV 4K with the A12 Bionic processor, support 
    for high frame rate HDR, HDMI 2.1, and Wi-Fi 6. Its HDMI port supports ARC and eARC, which allows 
    other sources plugged into the television to output audio through Apple TV, including to Bluetooth 
    speakers like HomePod.[67] It also has the ability to pair with the ambient light sensor on iPhones 
    with Face ID to optimize its color output, a feature that was also extended to older Apple TVs with tvOS 
    14.5. AirPlay supports high frame rate HDR playback, allowing videos shot on the iPhone 12 Pro in Dolby 
    Vision 4K 60fps to be mirrored in full resolution. Following the announcement, the previous Apple TV 
    4K with an A10X Fusion chip was discontinued.''')
            else:
                print("You entered an invalid Entry. Please try again.")
            
    elif a=='5':
        print(''' 
        Designed by Apple In California” chronicles 20 years of Apple design through 450 photographs of Apple products and the processes used to make them. 
        A visual history spanning iMac to Apple Pencil, complete with descriptions of innovative materials and techniques, 
        it captures every detail with honesty and intention. 
        It’s a hardcover edition, bound in linen, and is available in two sizes: 
        $199 for a smaller 10.20" x 12.75" version, and $299 for a larger 13" x 16.25" edition. 
        The book is simply titled Designed by Apple in California — a name that somehow manages to be 
        both humble and incredibly pretentious at the same time.''')
    elif a=="#":
        print("It was fun helping you. please visit again.")
        exit()
    else:
        print("You entered an invalid Entry. Please try again.")