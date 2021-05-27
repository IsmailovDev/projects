from telebot import types ,TeleBot
import config
import random
import baza
import sinov
tugmalar = types.InlineKeyboardMarkup(row_width = True)
for kanal in config.kanallar:
    tugmalar.add(types.InlineKeyboardButton(text = kanal[0],url = kanal[1]))
bot = TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start(message):
    
    baza.start(message.from_user.id)
    try:
        text = f'<b><pre>🛑QOIDALAR</pre></b>\n😁Xush Kelibsiz\n<b>{message.from_user.first_name}</b>\n________________________________\n👨🏻‍🎓🧑🏻‍🎓Agar siz testda qatnashmoqchi bo`lsangiz 👇🏻\n\n<b>/start -> kod</b> <i>absdba</i> \n\n<b>❗️Kod o`qituvchi tomonidan berilishi shart!</b>\n________________________________\n👨🏼‍🏫👩🏻‍🏫Agar siz test Oluvchi bo`lsangiz 👇🏻\n\n<b>/start -> </b><i>abcdab...</i>\n       '
        if sinov.member(message.from_user.id):
            for ini in config.photo:
                if ini[1]=='<b>9</b>\n':
                    ini[1]+='\n________________'+text
                bot.send_photo(message.from_user.id,ini[0],caption=ini[1],parse_mode='html')
            
           # bot.send_message(message.from_user.id,f'<b><pre>🛑QOIDALAR</pre></b>\n😁Xush Kelibsiz\n<b>{message.from_user.first_name}</b>\n________________________________\n👨🏻‍🎓🧑🏻‍🎓Agar siz testda qatnashmoqchi bo`lsangiz 👇🏻\n\n<b>/start -> kod</b> <i>absdba</i> \n\n<b>❗️Kod o`qituvchi tomonidan berilishi shart!</b>\n________________________________\n👨🏼‍🏫👩🏻‍🏫Agar siz test Oluvchi bo`lsangiz 👇🏻\n\n<b>/start -> </b><i>abcdab...</i>\n       ', parse_mode = 'html')
        else:
            bot.send_message(message.from_user.id,f"🤖Assalomu Alaykum <b>{message.from_user.first_name}</b>\n<i>⚠️Botimizdan Foydalanish Imkoniyatiga Ega Bo`lish Uchun \n📢Ushbu Kanallarga Obuna Bo`ling👇🏻</i>",parse_mode='html',reply_markup= tugmalar)
    except:
        print('xato startda')
@bot.message_handler(content_types=['text'])
def text(message):
    if message.from_user.id == 1272567697 and message.text == 'Hammasini Yo`q Qil':
        bot.send_message(1272567697,str(baza.clearbase()))
    if sinov.member(message.from_user.id):    
        try:
            takror = 0
            tj = 0
            nj = ''
            id = message.from_user.id
            habar = (message.text).lower().replace(' ','').replace('\n','')
            tasodif = random.randint(1000,9999)

            if tasodif in baza.tkodlist():
                    tasodif = random.randint(1000,9999)
            if str(habar).isalpha():
                baza.addtable(id)
                print(habar)
                baza.addtest(id,tasodif,habar)
                
                bot.send_message(id,f'📎Test kodi: <b>{tasodif}</b>\n👨🏻‍🎓🧑🏻‍🎓Testda <b>qatnashuvchilar</b> quyidagi holatda test javoblarini yuborishlari lozim 👇🏻\n🤖 @{bot.get_me().username} -> /start -> <b>{tasodif}abcad...</b>\n👩🏻‍🏫👨🏼‍🏫O`qituvchi: @{message.from_user.username}',parse_mode = 'html')
            
            elif int(habar[:4]) in baza.tkodlist():
                if baza.finduserid(int(habar[:4]),message.from_user.id):
                    bot.send_message(message.from_user.id,f"🛑<b>Siz {habar[:4]} Kodli Testda Oldin Qatnashganligingiz Sababli \nQayta Topshira Olmaysiz!</b>",parse_mode='html')
                else:
                    if len(baza.datanswershow(habar[:4]))!= len(habar)-4:
                        bot.send_message(id, f'🆘<b>Nomutanosiblik</b> \n📄Javoblar soni <b>{len(baza.datanswershow(habar[:4]))}🤔</b>siz kiritgan javoblar soni <b>{len(habar)-4}</b> ta',parse_mode = 'html')
                    else:
                        markup = types.InlineKeyboardMarkup()
                        markup.add(types.InlineKeyboardButton(f'📝{habar[:4]} Kodli Testni yakunlash', callback_data=habar[:4]))
                        markup.add(types.InlineKeyboardButton('🗂Barchasini yakunlash', callback_data=baza.kod_usershow(habar[:4])))
                        for i in baza.datanswershow(habar[:4]):
                
                            if i == habar[takror+4:takror+5]:
                                tj +=1
                            else:
                                nj+=str(takror+1)+','
                            takror+=1
                        bot.send_message(id, f'<b>{message.from_user.first_name}</b>\n🔍Natija: \n✅To`g`ri javoblar soni: <b>{tj}</b>\n❌Noto`g`ri javoblar soni: <b>{len(baza.datanswershow(habar[:4])) - tj}</b> ta\n♻️ @{bot.get_me().username}',parse_mode='html')
                        print(str(habar[:4]),str(message.from_user.first_name),str(message.from_user.username),str(nj))
                        baza.addstudent(str(habar[:4]),str(message.from_user.first_name),str(message.from_user.username),str(nj),str(message.from_user.id))
                        baza.tkod_userid(habar[:4],id,nj)
                        bot.send_message(baza.kod_usershow(int(message.text[:4])),f'🙋🏻‍♂️🙋🏻<b>{message.from_user.first_name}</b>\n🔍Natija: \n✅To`g`ri javoblar soni: <b>{tj}</b>\nNoto`g`ri javoblar soni: <b>{len(baza.datanswershow(habar[:4])) - tj}</b> ta\n❌Noto`g`ri javoblar ro`yxati: <b>{nj}</b>\n♻️ @{bot.get_me().username}',reply_markup=markup,parse_mode='html')
            else:
                bot.send_message(id , '<b>❗️Bunday malumot bazada yo`q?!</b>',parse_mode='html')
        except:
            bot.send_message(id,f'<b><pre>🛑QOIDALAR</pre></b>\n😁Xush Kelibsiz\n<b>{message.from_user.first_name}</b>\n________________________________\n👨🏻‍🎓🧑🏻‍🎓Agar siz testda qatnashmoqchi bo`lsangiz 👇🏻\n\n<b>/start -> kod</b> <i>absdba</i> \n\n<b>❗️Kod o`qituvchi tomonidan berilishi shart!</b>\n________________________________\n👨🏼‍🏫👩🏻‍🏫Agar siz test Oluvchi bo`lsangiz 👇🏻\n\n<b>/start -> </b><i>abcdab...</i>\n       ',parse_mode = 'html')
    else:
        bot.send_message(id,f"Assalomu Alaykum <b>{message.from_user.first_name}</b>\nBotdan foydalanaish Imkoniyatiga Ega Bo`lish Uchun \nUshbu Kanallarga Obuna Bo`ling👇🏻",reply_markup= tugmalar)
@bot.callback_query_handler(func=lambda call:True)
def back(call):
    if sinov.member(call.from_user.id):  
        if call.data == str(call.from_user.id):
            delusers1 = []
            try: 
                que = ''
                print(111111111111111111111)
                if baza.give_tkod(call.data):
                    for bik in baza.give_tkod(call.data):
                        for net in baza.get_studentid(bik):  
                            if sinov.usertekshiruvi(net[0]) and sinov.member(net[0]):
                            
                                print(net[0])
                                if net[1]:
                                    bot.send_message(net[0],f"⏰Noto`g`ri javoblar: <b>{net[1]}</b>\n♻️@{bot.get_me().username}",parse_mode='html')
                                else:
                                    pass
                            else:
                                delusers1.append(baza.give_del_user(bik,net[0]))
                                baza.delpupil(bik,net[0])
                    for i in baza.give_tkod(call.data):
                        print(111111111111111111111)
                        print(i)

                        natija = baza.give_natija(i)
                        print(natija)
                        
                        que += (f'\n________________________\nKod: <b>{i}</b>\nJavoblar: <b>{baza.datanswershow(i)}</b>\n_____________________\n'+str(natija))
                        print(que)
                    que=f"🏆O`qituvchi:<b>{call.from_user.first_name}</b>"+que   
                    bot.send_message(call.from_user.id, que,parse_mode='html')
                    que = ''
                    for i in delusers1:
                        que+=i+'\n'
                        
                    bot.send_message(call.from_user.id,'👌🏻<b>Barcha testlar to`xtatildi...</b>',parse_mode='html')
                    if que  == '\n':
                        bot.send_message(call.from_user.id,f'{que}\nUshbu Ro`yxatdagi <b>O`quvchilar</b> spam uchun testda belgilanmadi!!!',parse_mode='html')
                    else:
                        pass
                else:
                    pass
                try:
                    baza.deletetable(call.from_user.id)
                except:
                    pass
            except:
                bot.send_message(call.from_user.id,'<b>⁉️Sizda testlar yo`q</b>',parse_mode='html')
        elif call.data:
            delusers = []
            bot.send_message(call.from_user.id, call.data)
            try:
                for net in baza.get_studentid(call.data):  
                    if sinov.usertekshiruvi(net[0]) and sinov.member(net[0]):
                        print(net[0])
                        if net[1]:
                            bot.send_message(net[0],f"⏰Noto`g`ri javoblar: <b>{net[1]}</b>\n♻️@{bot.get_me().username}",parse_mode='html')
                        else:
                            pass
                    else:
                        delusers.append(baza.give_del_user(call.data,net[0]))
                        baza.delpupil(call.data,net[0]) 
                natija = f'🏆O`qituvchi:<b>{call.from_user.first_name}</b>\n________________________\nKod: <b>{call.data}</b>\nJavoblar: <b>{baza.datanswershow(call.data)}</b>\n___________________\n'+ str(baza.give_natija(call.data)) +f'@{bot.get_me().username}'                 
                bot.send_message(call.from_user.id, natija,parse_mode='html')
                bot.send_message(call.from_user.id, f"✅<b>{call.data}</b> kodli test o`chirildi...",parse_mode = 'html')
                que = ''
                for i in delusers:
                    que+=i+'\n'
                print(que,'554545')
                if que == '\n':
                    bot.send_message(call.from_user.id,f'{que}\nUshbu Ro`yxatdagi <b>O`quvchilar</b> spam uchun testda belgilanmadi!!!',parse_mode='html') 
                else:
                    pass
                if baza.exprement(baza.kod_usershow(call.data)):
                    if len(baza.exprement(baza.kod_usershow(call.data)))==1:
                        bot.send_message(call.from_user.id, f'Sizda <b>Testlar </b>qolmadi...',parse_mode = 'html')

                        
                    else:
                        
                        bot.send_message(call.from_user.id, f'Sizda <b>{len(baza.exprement(baza.kod_usershow(call.data)))-1}</b> ta test qoldi.',parse_mode = 'html')
                        

                else:
                    baza.deletetable(call.from_user.id)
                baza.deletetest(call.from_user.id,call.data)
                if baza.give_tkod(call.from_user.id):
                    pass
                else:
                    baza.deletetable(call.from_user.id)
            except:
                bot.send_message(call.from_user.id,'⛔️<b>Allaqachon bu test o`chirilgan?!</b>',parse_mode='html')
    else:
        messages = "Siz Avval Ushbu Kanalga obuna bo`lishingiz <b>Shart</b>"
        
      
        bot.send_message(call.from_user.id,messages,parse_mode='html')  
bot.polling()
