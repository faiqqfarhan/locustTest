from locust import HttpUser, between, task
import string
import random
EL_SERVER = 'http://el-pr105.sms.dev.unifonic.com/'
ARABIC_WORDLIST = '،؍؎؛ ؞؟ؠءآأؤإئابةتثجحخدذرزسشصضطظعغػؼؽؾؿـفقكلمنهوى٠١٢٣٤٥٦٧٨٩٪٫٬٭ٮٯٰٱٲٳٴٵٶٷٸٹٺٻټٽپٿڀځڂڃڄڅچڇڈډڊڋڌڍڎڏڐڑڒړڔڕږڗژڙښڛڜڝڞڟڠڡڢڣڤڥڦڧڨکڪګڬڭڮگڰڱڲڳڴڵڶڷڸڹںڻڼڽھڿۀہۂۃۄۅۆۇۈۉۊۋیۍێۏېۑےۓ۔ۮۯ۰۱۲۳۴۵۶۷۸۹ۺۻۼ۽۾ۿ'
APPSID = '6v253153s1g7831s5'
SENDERID = 'sender'
RECIPIENT = '00966560246635'
class APIUser(HttpUser):
  wait_time = between(0, 2)
  @task()
  def send_english_msg(self):
 url = EL_SERVER + "/provisioning/GetAccount"
 num_of_chars = random.randint(1, 150)
    body = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=num_of_chars))
 data = {
      "AppSid": APPSID,
      "Recipient": RECIPIENT,
      "Body": body,
      "SenderID": SENDERID
    }
    self.client.post( url, data=data )
  @task()
  def send_arabic_single_part(self):
    url = EL_SERVER + "/rest/SMS/messages"
    num_of_chars = random.randint(1, 150)
    body = ''.join(random.choices(ARABIC_WORDLIST + ' ', k=num_of_chars))
    data = {
      "AppSid": APPSID,
      "Recipient": RECIPIENT,
      "Body": body,
      "SenderID": SENDERID
    }
    self.client.post( url, data=data )
  # send_arabic_multi_part
  # send_eng_single_part
  # send_eng_multi_part
  # send_special_char_multi_part
  # send_ten_multi_part_arabic_eng