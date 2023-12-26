from flask import Flask, render_template, request, redirect, url_for 
from database_connect import db_connect, cursor
app = Flask(__name__)

msg = 'Nekas'
###########################################################

@app.route('/')
def main_page():
    server = db_connect()
    cur = cursor()
    cur.execute('SELECT zip,nosaukums FROM omniva;') 
    pakomati = cur.fetchall()
    server.close()
    cur.close()
    return render_template('index.html', data=pakomati)

@app.route('/update', methods=['POST']) 
def update(): 
    # Get the data from the form 
    zip = request.form['zip'] 
    nosaukums = request.form['nosaukums'] 
  
    # Update the data in the table 
    server = db_connect()
    cur = cursor()
    cur.execute('''UPDATE omniva SET nosaukums='%s' WHERE zip=%s;''', (nosaukums, zip)) 
  
    print ('Bla')
    print ('''UPDATE omniva SET nosaukums='%s' WHERE zip=%s;''', (nosaukums, zip))


    # commit the changes 
    server.commit() 
    cur.close()
    server.close()
    return redirect(url_for('main_page')) 

@app.route('/reset', methods=['POST'])
def reset():
    server = db_connect()
    cur = cursor()

    # Create / Empty table "Omniva"
    cur.execute("CREATE TABLE IF NOT EXISTS omniva (zip integer NOT NULL, nosaukums varchar(250) NOT NULL);") 
    cur.execute("TRUNCATE TABLE omniva;") 

    # Insert data into the table 
    cur.execute( 
        '''INSERT INTO omniva (zip, nosaukums) VALUES \
    (9101, 'Rīgas T/C Akropole pakomāts'), \
    (9102, 'Ventspils Poruka ielas RIMI pakomāts'), \
    (9103, 'Rīgas Āgenskalna RIMI pakomāts'), \
    (9104, 'Ilūkstes Pilskalnes ielas TOP pakomāts'), \
    (9105, 'Ādažu T/C Apelsīns pakomāts'), \
    (9106, 'Jaunolaines TOP pakomāts'), \
    (9107, 'Jūrmalas Dubultu TOP pakomāts'), \
    (9108, 'Liepājas Ganību ielas JYSK pakomāts'), \
    (9109, 'Rīgas Stirnu ielas RIMI pakomāts'), \
    (9110, 'Ulbrokas ELVI pakomāts'), \
    (9111, 'Rīgas A. Briāna ielas RIMI pakomāts'), \
    (9112, 'Rīgas Nīcgales ielas 53 T/C GREEN pakomāts'), \
    (9113, 'Rīgas T/C DOMINA pakomāts'), \
    (9114, 'Rīgas T/C Riga Plaza pakomāts'), \
    (9115, 'Rīgas Brīvības ielas 35 pakomāts'), \
    (9116, 'Rīgas Autoostas pakomāts'), \
    (9117, 'Piņķu Elvi pakomāts'), \
    (9118, 'Viļānu Brīvības ielas pakomāts'), \
    (9119, 'Valmieras Nākotnes ielas Maxima X pakomāts'), \
    (9120, 'Tukuma Kurzemes ielas 36 Maxima XX pakomāts'), \
    (9121, 'Salacgrīvas Maxima X pakomāts'), \
    (9122, 'Rīgas Lidoņu ielas Mego pakomāts'), \
    (9123, 'Rīgas Kurzemes prospekta Mego pakomāts'), \
    (9124, 'Lielvārdes TOP pakomāts'), \
    (9125, 'Ikšķiles Mini RIMI pakomāts'), \
    (9126, 'Grobiņas TOP pakomāts'), \
    (9127, 'Baldones Mego pakomāts'), \
    (9128, 'Rīgas Tilta ielas RIMI pakomāts'), \
    (9129, 'Rīgas Prūšu ielas 2 Mego pakomāts'), \
    (9130, 'Priekules TOP pakomāts'), \
    (9131, 'Jelgavas T/C Valdeka pakomāts'), \
    (9133, 'Ogres Rīgas ielas RIMI pakomāts'), \
    (9134, 'Valdlauču TOP pakomāts'), \
    (9135, 'Talsu Rīgas ielas Maxima XX pakomāts'), \
    (9136, 'Rojas Maxima X pakomāts'), \
    (9137, 'Cēsu Gaujas ielas Maxima X pakomāts'), \
    (9138, 'Ropažu Lats Pakomāts'), \
    (9139, 'Strenču TOP pakomāts'), \
    (9140, 'Inčukalna Aibe pakomāts'), \
    (9141, 'Kokneses Lats pakomāts'), \
    (9142, 'Jūrmalas Slokas T/C Liedags pakomāts'), \
    (9143, 'Rīgas Duntes ielas Neste pakomāts'), \
    (9144, 'Rīgas Valsts Ieņēmumu Dienesta pakomāts'), \
    (9145, 'Mālpils Pirts ielas TOP pakomāts'), \
    (9146, 'Rīgas Vecmīlgrāvja Maxima X pakomāts'), \
    (9147, 'Rīgas Kalnciema ielas RIMI pakomāts'), \
    (9148, 'Vangažu Aibe pakomāts'), \
    (9149, 'Saulkrastu TOP pakomāts'), \
    (9150, 'Rīgas Kleistu ielas Mego pakomāts'), \
    (9151, 'Rīgas Parādes ielas Mego pakomāts'), \
    (9152, 'Raganas ELVI pakomāts'), \
    (9153, 'Ērgļu Zaļās ielas TOP pakomāts'), \
    (9154, 'Vecumnieku Lats pakomāts'), \
    (9155, 'Jaunmārupes Mazcenu alejas pakomāts'), \
    (9156, 'Elejas Astarte pakomāts'), \
    (9157, 'Viļakas Balvu ielas pakomāts'), \
    (9158, 'Auces TOP pakomāts'), \
    (9159, 'Rīgas T/C Elkor Plaza pakomāts'), \
    (9160, 'Rīgas Biķernieku ielas 16a MEGO pakomāts'), \
    (9161, 'Rīgas Jūrmalas gatves RIMI pakomāts'), \
    (9162, 'Kārsavas TOP pakomāts'), \
    (9163, 'Dundagas Citro pakomāts'), \
    (9164, 'Rīgas Murjāņu ielas MEGO pakomāts'), \
    (9165, 'Ķeguma ELVI pakomāts'), \
    (9166, 'Valmieras Rubenes ielas RIMI pakomāts'), \
    (9167, 'Viesītes TOP pakomāts'), \
    (9168, 'Zilupes TOP pakomāts'), \
    (9169, 'Rīgas A. Deglava 110 Rimi pakomāts'), \
    (9170, 'Jaunpils TOP pakomāts'), \
    (9171, 'Rīgas Leļļu teātra pakomāts'), \
    (9172, 'Rīgas Tēriņu ielas 55 pakomāts'), \
    (9173, 'Rīgas Miera ielas 2 pakomāts'), \
    (9174, 'Rīgas Brīvības gatves 386 Neste pakomāts'), \
    (9175, 'Rīgas Saharova ielas Maxima XXX pakomāts'), \
    (9176, 'Rīgas Rītupes ielas Maxima X pakomāts'), \
    (9177, 'Rīgas Mūkusalas Maxima XX pakomāts'), \
    (9178, 'Rīgas Katoļu ielas Neste pakomāts'), \
    (9179, 'Rīgas Prūšu ielas 22a Mego pakomāts'), \
    (9180, 'Rīgas T/C Aleja pakomāts '), \
    (9181, 'Rīgas T/C IXO pakomāts'), \
    (9182, 'Babītes ELVI pakomāts'), \
    (9183, 'Aknīstes VESKO pakomāts'), \
    (9184, 'Upesciema Lats pakomāts'), \
    (9185, 'Rīgas Jaunciema gatves Maxima X pakomāts'), \
    (9186, 'Madlienas ELVI pakomāts'), \
    (9187, 'Lapmežciema Citro pakomāts'), \
    (9188, 'Rīgas T/C Gaiļezers pakomāts'), \
    (9189, 'Salaspils Rīgas ielas AIBE pakomāts'), \
    (9190, 'Skrīveru TOP pakomāts'), \
    (9191, 'Rīgas Vecāķu ELVI pakomāts'), \
    (9192, 'Alojas Mini TOP pakomāts'), \
    (9193, 'Augšlīgatnes ELVI pakomāts'), \
    (9194, 'Cēsu T/C Globuss pakomāts'), \
    (9195, 'Madonas Saules ielas 4 pakomāts'), \
    (9196, 'Straupes VIADA pakomāts'), \
    (9197, 'Valmieras Rīgas ielas TOP pakomāts'), \
    (9198, 'Jelgavas T/C Pilsētas Pasāža pakomāts'), \
    (9199, 'Jelgavas Rūpniecības ielas ELVI pakomāts'), \
    (9201, 'Bauskas Pionieru ielas RIMI pakomāts'), \
    (9202, 'Dobeles Zaļās ielas Maxima X pakomāts'), \
    (9203, 'Skaistkalnes VESKO pakomāts'), \
    (9204, 'Engures Citro pakomāts'), \
    (9205, 'Kuldīgas Gravas ielas ELVI pakomāts'), \
    (9206, 'Liepājas Ganību ielas ELVI pakomāts'), \
    (9207, 'Pāvilostas TOP pakomāts'), \
    (9208, 'Saldus Striķu ielas Maxima X pakomāts'), \
    (9209, 'Ugāles Lats pakomāts'), \
    (9210, 'Ventspils Celtnieku ielas ELVI pakomāts'), \
    (9211, 'Daugavpils Cialkovska ielas Lats pakomāts'), \
    (9212, 'Jaunjelgavas Mini Top pakomāts'), \
    (9213, 'Jēkabpils T/C Sēlija pakomāts'), \
    (9214, 'Neretas TOP pakomāts'), \
    (9215, 'Rīgas Valdeķu ielas 10 Maxima X pakomāts'), \
    (9216, 'Rēzeknes Kr. Valdemāra ielas Mego pakomāts'), \
    (9217, 'Lubānas O. Kalpaka ielas Vesko pakomāts'), \
    (9218, 'Jūrmalas Asaru Senās bodes pakomāts'), \
    (9219, 'Salaspils Rīgas ielas MEGO pakomāts'), \
    (9227, 'Gulbenes Dzelzceļa ielas 14 pakomāts'), \
    (9228, 'Alūksnes Pils ielas TOP pakomāts'), \
    (9229, 'Mārupes Rožu ielas 2 pakomāts'), \
    (9230, 'Jūrmalas Mellužu Dārzu ielas 55A pakomāts'), \
    (9231, 'Rīgas Berģu ielas Senās Bodes pakomāts'), \
    (9232, 'Berģu SKY pakomāts'), \
    (9233, 'Rīgas T/C Venta pakomāts'), \
    (9234, 'Garkalnes Lats pakomāts'), \
    (9235, 'Siguldas Kr. Barona ielas Beta pakomāts'), \
    (9236, 'Nīcas Lats pakomāts'), \
    (9237, 'Liepājas P. Brieža ielas 14 TOP pakomāts'), \
    (9238, 'Talsu Dundagas ielas Citro pakomāts'), \
    (9239, 'Talsu T/C Talsu Centrs pakomāts'), \
    (9240, 'Tīnūžu Senās Bodes pakomāts'), \
    (9241, 'Saulkalnes Lats pakomāts'), \
    (9242, 'Liepājas O. Kalpaka ielas 74 pakomāts'), \
    (9243, 'Tukuma Alīnes ielas TOP pakomāts'), \
    (9244, 'Tukuma T/C Aplis pakomāts'), \
    (9245, 'Ķekavas T/C Dālderi pakomāts'), \
    (9246, 'Daugmales ELVI pakomāts'), \
    (9247, 'Kadagas T/C Kadaga pakomāts'), \
    (9248, 'Zvejniekciema Mego pakomāts'), \
    (9249, 'Plakanciema pakomāts'), \
    (9250, 'Rīgas Liepājas ielas Maxima X pakomāts'), \
    (9251, 'Rīgas Kurzemes prospekta 15a Neste pakomāts'), \
    (9252, 'Rīgas Bolderājas Lats pakomāts'), \
    (9253, 'Rīgas Čiekurkalna MEGO pakomāts'), \
    (9254, 'Rīgas Viestura prospekta 35a TOP pakomāts'), \
    (9255, 'Siguldas L. Paegles ielas Maxima pakomāts'), \
    (9256, 'Siguldas T/C Gāles Nams pakomāts'), \
    (9257, 'Jelgavas Uzvaras ielas Lats pakomāts'), \
    (9258, 'Ozolnieku ELVI pakomāts'), \
    (9259, 'Cēsu Gaujas ielas TOP pakomāts'), \
    (9260, 'Cēsu T/C SOLO pakomāts'), \
    (9261, 'Rīgas Juglas ielas 25 MINI RIMI pakomāts'), \
    (9262, 'Ogres Skolas ielas 4 pakomāts'), \
    (9263, 'Mērsraga Citro pakomāts'), \
    (9264, 'Kolkas Citro pakomāts'), \
    (9265, 'Jēkabpils T/C Sprīdītis pakomāts'), \
    (9266, 'Aizkraukles TOP pakomāts'), \
    (9267, 'Rīgas Zemitāna ielas 9 GRĪZIŅDĀRZS pakomāts'), \
    (9268, 'Valmieras Stacijas ielas 33 pakomāts'), \
    (9269, 'Valmieras Miera ielas TOP pakomāts'), \
    (9271, 'Ventspils Inženieru ielas MEGO pakomāts'), \
    (9272, 'Daugavpils 18. novembra ielas Lats pakomāts'), \
    (9273, 'Daugavpils Gaismas ielas TOP pakomāts'), \
    (9274, 'Rīgas Graudu ielas Mego pakomāts'), \
    (9275, 'Ulbrokas TOP pakomāts'), \
    (9276, 'Zaķumuižas pakomāts'), \
    (9277, 'Rīgas Saharova ielas 2 MEGO pakomāts'), \
    (9278, 'Rīgas Sporta Pils dārzu pakomāts'), \
    (9279, 'Rīgas T/C Sāga pakomāts'), \
    (9280, 'Bauskas Upmalas ielas TOP pakomāts'), \
    (9281, 'Rīgas Brīvības ielas 78a pakomāts'), \
    (9282, 'Rīgas Baltāsbaznīcas ielas MEGO pakomāts'), \
    (9283, 'Medemciema pakomāts'), \
    (9284, 'Kalnciema Aibe pakomāts'), \
    (9285, 'Sabiles Citro pakomāts'), \
    (9286, 'Rīgas Stabu ielas 58 pakomāts'), \
    (9287, 'Jēkabpils Nameja ielas TOP pakomāts'), \
    (9288, 'Varakļānu TOP pakomāts'), \
    (9290, 'Valkas Raiņa ielas Maxima X pakomāts'), \
    (9291, 'Preiļu Rīgas ielas MEGO pakomāts'), \
    (9292, 'Mārupes Dzirnieku ielas 24 pakomāts'), \
    (9293, 'Maltas Lats pakomāts'), \
    (9294, 'Jelgavas Lielās ielas ELVI pakomāts'), \
    (9295, 'Rīgas Hipokrāta ielas FIX PRICE pakomāts'), \
    (9296, 'Cesvaines TOP pakomāts'), \
    (9297, 'Madonas Raiņa ielas 34 pakomāts'), \
    (9298, 'Mazsalacas pakomāts'), \
    (9299, 'Limbažu Pasta ielas pakomāts'), \
    (9501, 'Sauriešu DELFĪNS pakomāts'), \
    (9502, 'Rīgas Daugavgrīvas ielas TOP pakomāts'), \
    (9503, 'Ikšķiles ELVI pakomāts'), \
    (9504, 'Rīgas Buļļu ielas 35 Aibe pakomāts'), \
    (9505, 'Balvu Tautas ielas 1 pakomāts'), \
    (9506, 'Raunas TOP pakomāts'), \
    (9507, 'Jūrmalas Ķemeru TOP pakomāts'), \
    (9508, 'Suntažu AIBE pakomāts'), \
    (9509, 'Ķekavas Rīgas ielas RIMI pakomāts'), \
    (9510, 'Ogres Kartona fabrikas pakomāts'), \
    (9511, 'Rēzeknes Dārzu ielas Citro pakomāts'), \
    (9512, 'Rīgas Maskavas ielas 427b Neste pakomāts'), \
    (9513, 'Saldus Kalna ielas AIBE KAIVA pakomāts'), \
    (9514, 'Rīgas Bērnu slimnīcas pakomāts'), \
    (9515, 'Apes TOP pakomāts'), \
    (9516, 'Smiltenes Rīgas ielas TOP pakomāts'), \
    (9517, 'Salaspils Miera ielas AIBE pakomāts'), \
    (9518, 'Dobeles Muldavas ielas TOP pakomāts'), \
    (9519, 'Rīgas Vaidelotes ielas RIMI pakomāts'), \
    (9520, 'Rīgas T/C Galleria Riga pakomāts'), \
    (9521, 'Rīgas BARONS KVARTĀLS pakomāts'), \
    (9522, 'Rīgas Kalpaka bulvāra 14A pakomāts'), \
    (9523, 'Salaspils Rīgas ielas TOP pakomāts'), \
    (9524, 'Ādažu Rīgas gatves ELVI pakomāts'), \
    (9525, 'Kalngales ELVI pakomāts'), \
    (9526, 'Katlakalna pakomāts'), \
    (9527, 'Mārupes Lielās ielas ELVI pakomāts'), \
    (9528, 'Rīgas Avotu ielas 17 pakomāts'), \
    (9529, 'Rīgas T/C Ozols pakomāts'), \
    (9530, 'Rīgas Biķernieku ielas 98 Mego pakomāts'), \
    (9531, 'Tukuma Kurzemes ielas 2A Mego pakomāts'), \
    (9532, 'Pūres Citro pakomāts'), \
    (9533, 'Rīgas Dammes ielas Mego pakomāts'), \
    (9534, 'Rīgas RIMI Olimpiskais Centrs pakomāts'), \
    (9535, 'Stendes Brīvības ielas Citro pakomāts'), \
    (9536, 'Kuldīgas Stendes ielas Citro pakomāts'), \
    (9537, 'Rīgas Struktoru ielas Lats pakomāts'), \
    (9538, 'Rīgas PEPSI CENTRS pakomāts'), \
    (9539, 'Liepājas Kuršu laukuma 10 pakomāts'), \
    (9540, 'Rīgas Lāčplēša ielas 57 pakomāts'), \
    (9541, 'Rīgas Ezermalas ielas 2C pakomāts'), \
    (9543, 'Priekuļu Aibe pakomāts'), \
    (9544, 'Rīgas Dzelzavas ielas 78 RIMI pakomāts'), \
    (9545, 'Rīgas E. Birznieka-Upīša ielas 19 pakomāts'), \
    (9546, 'Rīgas Zalves ielas TOP pakomāts'), \
    (9547, 'Rīgas Valmieras ielas 2 pakomāts'), \
    (9548, 'Jūrmalas Priedaines Lielā prospekta 10 pakomāts'), \
    (9549, 'Jūrmalas Majoru J. Pliekšāna ielas TOP pakomāts'), \
    (9550, 'Iecavas TOP pakomāts'), \
    (9551, 'Rīgas Maskavas ielas 256B RIMI pakomāts'), \
    (9552, 'Druvas ELVI pakomāts'), \
    (9553, 'Jelgavas Tērvetes ielas TOP pakomāts'), \
    (9554, 'Liepājas Sila ielas TOP pakomāts'), \
    (9555, 'Saldus Lielās ielas Lats pakomāts'), \
    (9556, 'Rēzeknes Stacijas ielas 20A pakomāts'), \
    (9557, 'Madonas Saules ielas 39B pakomāts'), \
    (9558, 'Cēsu Viestura ielas TOP pakomāts'), \
    (9559, 'Ogres Mālkalnes prospekta 3 pakomāts'), \
    (9560, 'Saulkrastu Ainažu ielas ELVI pakomāts'), \
    (9561, 'Naukšēnu Lats pakomāts'), \
    (9562, 'Rīgas Artilērijas ielas 40 pakomāts'), \
    (9563, 'Jelgavas Meiju ceļa Aibe pakomāts'), \
    (9564, 'Ezeres ELVI pakomāts'), \
    (9565, 'Smiltenes Daugavas ielas TOP pakomāts'), \
    (9566, 'Daugavpils Viestura ielas Mego pakomāts'), \
    (9567, 'Rīgas Brīvības gatves 404 RIMI pakomāts'), \
    (9568, 'Rīgas Āgenskalna ielas 29A pakomāts'), \
    (9569, 'Olaines Stacijas ielas RIMI pakomāts'), \
    (9570, 'Jumpravas Lats pakomāts'), \
    (9571, 'Rīgas T/C Augusts pakomāts'), \
    (9572, 'Jūrmalas Kauguru Raiņa ielas Mini RIMI pakomāts'), \
    (9573, 'Rīgas Purvciema ielas Beta pakomāts'), \
    (9574, 'Rīgas Vaidavas ielas RIMI pakomāts'), \
    (9575, 'Dobeles Krasta ielas TOP pakomāts'), \
    (9576, 'Rīgas Ropažu ielas 63 pakomāts'), \
    (9577, 'Valdemārpils Lielās ielas 17A pakomāts'), \
    (9578, 'Daugavpils 18. novembra ielas RIMI pakomāts'), \
    (9579, 'Baldones TOP pakomāts'), \
    (9580, 'Jūrmalas Kauguru Engures ielas Maxima pakomāts'), \
    (9581, 'Jaunpiebalgas pakomāts'), \
    (9582, 'Rēzeknes Dārzu ielas ELFI pakomāts'), \
    (9583, 'Ogres Brīvības ielas 19 pakomāts'), \
    (9584, 'Jūrmalas Bulduru tirgus pakomāts'), \
    (9585, 'Slampes pakomāts'), \
    (9586, 'RĀMKALNI pakomāts'), \
    (9587, 'Piņķu Rīgas ielas RIMI pakomāts'), \
    (9588, 'Ventspils Talsu ielas Citro pakomāts'), \
    (9589, 'Valmieras Fabrikas ielas RIMI pakomāts'), \
    (9590, 'Liepas TOP pakomāts'), \
    (9591, 'Rīgas Pētersalas ielas Maxima pakomāts'), \
    (9901, 'Rīgas T/C AKROPOLE Alfa pakomāts'), \
    (9902, 'Rīgas Anniņmuižas bulvāra RIMI pakomāts'), \
    (9903, 'Rīgas P. Brieža ielas RIMI pakomāts'), \
    (9904, 'Rīgas Deglava ielas Maxima XXX pakomāts'), \
    (9905, 'Rīgas T/C Dole pakomāts'), \
    (9906, 'Rīgas Saharova ielas 14 Mego pakomāts'), \
    (9907, 'Rīgas Mazās stacijas ielas Drogas pakomāts'), \
    (9908, 'Rīgas Gramzdas RIMI pakomāts'), \
    (9909, 'Rīgas G. Astras ielas VIADA pakomāts'), \
    (9911, 'Rīgas T/C Mols pakomāts'), \
    (9912, 'Rīgas Vienības gatves 144 Neste pakomāts'), \
    (9914, 'Rīgas T/C Spice pakomāts'), \
    (9915, 'Rīgas T/C Juglas Centrs pakomāts'), \
    (9916, 'Daugavpils T/C Aveņu centrs pakomāts'), \
    (9917, 'Liepājas T/C Baata pakomāts'), \
    (9918, 'Daugavpils T/C Ditton pakomāts'), \
    (9919, 'Jelgavas T/C RAF pakomāts'), \
    (9920, 'Jūrmalas Kauguru RIMI pakomāts'), \
    (9921, 'Cēsu Valmieras ielas Maxima XX pakomāts'), \
    (9922, 'Rēzeknes Atbrīvošanas alejas Maxima XX pakomāts'), \
    (9923, 'Ventspils Ganību ielas Mego pakomāts'), \
    (9924, 'Jēkabpils Vienības ielas Mego pakomāts'), \
    (9925, 'Ogres T/C Ogres prestižs pakomāts'), \
    (9926, 'Liepājas Rožu laukuma pakomāts'), \
    (9927, 'Tukuma Pasta ielas RIMI pakomāts'), \
    (9928, 'Valmieras T/C Valleta pakomāts'), \
    (9929, 'Jelgavas T/C Vivo centrs pakomāts'), \
    (9930, 'Kuldīgas Sūru ielas RIMI pakomāts'), \
    (9931, 'Talsu Dundagas ielas RIMI pakomāts'), \
    (9932, 'Siguldas T/C Šokolāde pakomāts'), \
    (9933, 'Rīgas Biķernieku ielas RIMI pakomāts'), \
    (9934, 'Rīgas T/C Olimpia pakomāts'), \
    (9935, 'Rīgas T/C Damme pakomāts'), \
    (9936, 'Saldus Brīvības ielas Maxima XX pakomāts'), \
    (9937, 'Rīgas T/C A7 pakomāts'), \
    (9938, 'Liepājas Ziemeļu ielas RIMI pakomāts'), \
    (9939, 'Rīgas Kr. Valdemāra ielas 112 RIMI pakomāts'), \
    (9940, 'Bauskas Mini RIMI pakomāts'), \
    (9941, 'Dobeles Brīvības ielas RIMI pakomāts'), \
    (9942, 'Limbažu Maxima XX pakomāts'), \
    (9943, 'Jūrmalas Lielupes RIMI pakomāts'), \
    (9944, 'Madonas Rūpniecības ielas MINI RIMI pakomāts'), \
    (9946, 'Rīgas Bērnu pasaules RIMI pakomāts'), \
    (9947, 'Salaspils Skolas ielas RIMI pakomāts'), \
    (9948, 'Gulbenes Nākotnes ielas TOP pakomāts'), \
    (9949, 'Olaines T/C Prasme pakomāts'), \
    (9950, 'Aizkraukles T/C Iga pakomāts'), \
    (9951, 'Alūksnes Maxima X pakomāts'), \
    (9952, 'Ādažu Gaujas ielas Mini RIMI pakomāts'), \
    (9953, 'Ogres T/C Dauga pakomāts'), \
    (9954, 'Rīgas T/C Minska pakomāts'), \
    (9955, 'Smiltenes T/C Centrs pakomāts'), \
    (9956, 'Valkas T/C Walk pakomāts'), \
    (9957, 'Ventspils Tārgales ielas Mini RIMI pakomāts'), \
    (9958, 'Preiļu Brīvības ielas TOP pakomāts'), \
    (9959, 'Rīgas Vecmīlgrāvja RIMI pakomāts'), \
    (9960, 'Rīgas Bolderājas Mego pakomāts'), \
    (9961, 'Rīgas Ziepniekkalna MEGO pakomāts'), \
    (9962, 'Rīgas Dzelzavas ielas Mini RIMI pakomāts'), \
    (9963, 'Ventspils T/C Tobago pakomāts'), \
    (9964, 'Rīgas Āgenskalna Maxima X pakomāts'), \
    (9965, 'Rīgas T/C Origo pakomāts'), \
    (9966, 'Liepājas T/C Rietumu centrs pakomāts'), \
    (9967, 'Mārupes RIMI pakomāts'), \
    (9968, 'Rīgas Brīvības g. 253 Neste pakomāts'), \
    (9969, 'Jēkabpils Rīgas ielas Mini RIMI pakomāts'), \
    (9970, 'Baložu Mego pakomāts'), \
    (9971, 'Rīgas Ulbrokas ielas Maxima X pakomāts'), \
    (9972, 'Rīgas Grostonas ielas Maxima XXX pakomāts'), \
    (9974, 'Rēzeknes Galdnieku ielas RIMI pakomāts'), \
    (9975, 'Rīgas Botāniskā dārza Maxima pakomāts'), \
    (9976, 'Rīgas Mīlgrāvja ielas RIMI pakomāts '), \
    (9977, 'Rīgas S. Eizenšteina ielas 29 pakomāts'), \
    (9978, 'Ķekavas T/C Liiba pakomāts'), \
    (9979, 'Kandavas Citro pakomāts'), \
    (9980, 'Aizputes Zvaigžņu ielas AIBE pakomāts'), \
    (9981, 'Jelgavas Satiksmes ielas RIMI pakomāts'), \
    (9982, 'Balvu TOP pakomāts'), \
    (9983, 'Līvānu Rimi pakomāts'), \
    (9984, 'Krāslavas Maxima X pakomāts'), \
    (9985, 'Ludzas Stacijas ielas 30 pakomāts'), \
    (9986, 'Siguldas ELVI Vidus iela pakomāts'), \
    (9987, 'Iecavas Maxima X pakomāts'), \
    (9988, 'Carnikavas Mego pakomāts'), \
    (9989, 'Dagdas TOP pakomāts'), \
    (9990, 'Pļaviņu TOP pakomāts'), \
    (9991, 'Rūjienas TOP pakomāts'), \
    (9992, 'Skrundas ELVI pakomāts'), \
    (9993, 'Vecpiebalgas TOP pakomāts'), \
    (9994, 'Ozolnieku TOP pakomāts'), \
    (9995, 'Rīgas T/C ZOOM pakomāts'), \
    (9997, 'Brocēnu Citro pakomāts'), \
    (9998, 'Daugavpils Valkas ielas Mego pakomāts');''') 

    # commit the changes
    server.commit() 
    cur.close()
    server.close()

    return redirect(url_for('main_page')) 

if __name__ == '__main__': 
    app.run(debug=True) 