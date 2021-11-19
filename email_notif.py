import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment
import configparser

class Email:
      
      def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/config.ini")
        self.sender_email = self.config.get("EMAILKEYS", "from")
        self.receiver_email = self.config.get("EMAILKEYS", "to")
        self.password = self.config.get("EMAILKEYS", "password")

      def send_email_notif(self, path, initial_row, final_row):
        print("Sending email notification..")
        message = MIMEMultipart("alternative")
        message["Subject"] = "Google scholar scrape alert"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hello,

        This is an automated email generated because {{ path }} has been modified by the Google Scholar Scrape bot. The following lines have been added:
        {{placeholder}}"""
        html = """\
        <!doctype html>
        <html>

        <head>
          <meta name="viewport" content="width=device-width">
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <title>Google scholar scrape notification</title>
          <style>
            @media only screen and (max-width: 620px) {
              table[class=body] h1 {
                font-size: 28px !important;
                margin-bottom: 10px !important;
              }

              table[class=body] p,
              table[class=body] ul,
              table[class=body] ol,
              table[class=body] td,
              table[class=body] span,
              table[class=body] a {
                font-size: 16px !important;
              }

              table[class=body] .wrapper,
              table[class=body] .article {
                padding: 10px !important;
              }

              table[class=body] .content {
                padding: 0 !important;
              }

              table[class=body] .container {
                padding: 0 !important;
                width: 100% !important;
              }

              table[class=body] .main {
                border-left-width: 0 !important;
                border-radius: 0 !important;
                border-right-width: 0 !important;
              }

              table[class=body] .btn table {
                width: 100% !important;
              }

              table[class=body] .btn a {
                width: 100% !important;
              }

              table[class=body] .img-responsive {
                height: auto !important;
                max-width: 100% !important;
                width: auto !important;
              }
            }

            @media all {
              .ExternalClass {
                width: 100%;
              }

              .ExternalClass,
              .ExternalClass p,
              .ExternalClass span,
              .ExternalClass font,
              .ExternalClass td,
              .ExternalClass div {
                line-height: 100%;
              }

              .apple-link a {
                color: inherit !important;
                font-family: inherit !important;
                font-size: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
                text-decoration: none !important;
              }

              #MessageViewBody a {
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
              }

              .btn-primary table td:hover {
                background-color: #34495e !important;
              }

              .btn-primary a:hover {
                background-color: #34495e !important;
                border-color: #34495e !important;
              }
            }
          </style>
        </head>

        <body class=""
          style="background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
          <span class="preheader"
            style="color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0;">Google
            scholar bot</span>
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body"
            style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f6f6f6; width: 100%;"
            width="100%" bgcolor="#f6f6f6">
            <tr>
              <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;" valign="top">&nbsp;</td>
              <td class="container"
                style="font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; max-width: 580px; padding: 10px; width: 580px; margin: 0 auto;"
                width="580" valign="top">
                <div class="content"
                  style="box-sizing: border-box; display: block; margin: 0 auto; max-width: 580px; padding: 10px;">

                  <!-- START CENTERED WHITE CONTAINER -->
                  <table role="presentation" class="main"
                    style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; border-radius: 3px; width: 100%;"
                    width="100%">

                    <!-- START MAIN CONTENT AREA -->
                    <tr>
                      <td class="wrapper"
                        style="font-family: sans-serif; font-size: 14px; vertical-align: top; box-sizing: border-box; padding: 20px;"
                        valign="top">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0"
                          style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
                          width="100%">
                          <tr>
                            <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;" valign="top">
                              <img src="cid:header" height="100px" width="100%"
                                style="border: none; -ms-interpolation-mode: bicubic; max-width: 100%;"><br><br>
                              <p
                                style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">
                                Hello,</p>
                              <p
                                style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">
                                This is an automated email generated because <b><i>{{ path }}</i></b> has been modified
                                by the Google Scholar Scrape bot. The following lines have been added: </p>
                              <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="table-changes"
                                style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-color: lightsalmon;"
                                width="100%" bgcolor="lightsalmon">
                                <tbody>
                                  <tr>
                                    <td align="center" style="font-family: sans-serif; font-size: 14px; vertical-align: top;"
                                      valign="top">
                                      <table role="presentation" border="0" cellpadding="0" cellspacing="0"
                                        style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
                                        width="100%">
                                        <tbody>
                                          <tr>
                                            <td style="font-family: sans-serif; font-size: 14px; vertical-align: middle; text-align:center;"
                                              valign="middle">
                                              <p
                                                style="font-family: sans-serif; font-size: 16px; font-weight: bold; color: red; margin: 10px;">
                                                {{ placeholder }}</p>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>

                    <!-- END MAIN CONTENT AREA -->
                  </table>
                  <!-- END CENTERED WHITE CONTAINER -->

                  <!-- START FOOTER -->
                  <div class="footer" style="clear: both; margin-top: 10px; text-align: center; width: 100%;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0"
                      style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;"
                      width="100%">
                      <tr>
                        <td class="content-block"
                          style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; color: #999999; font-size: 12px; text-align: center;"
                          valign="top" align="center">
                          <span class="apple-link" style="color: #999999; font-size: 12px; text-align: center;">Bicycling plus
                            google scholar bot</span>
                        </td>
                      </tr>
                    </table>
                  </div>
                  <!-- END FOOTER -->

                </div>
              </td>
              <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;" valign="top">&nbsp;</td>
            </tr>
          </table>
        </body>

        </html>
        """


        # Open a file object to read the image file, the image file is located in the file path it provide.
        fp = open('email_template/header.png', 'rb')
        # Create a MIMEImage object with the above file object.
        msgImage = MIMEImage(fp.read())
        # Do not forget close the file object after using it.
        fp.close()
        # Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
        msgImage.add_header('Content-ID', '<header>')
        # Attach the MIMEImage object to the email body.
        message.attach(msgImage)
        # Turn these into plain/html MIMEText objects
        if (initial_row == final_row):
          placeholder_lines = "Line " + str(initial_row)
        else:
          placeholder_lines = "Lines " + \
              str(initial_row) + " to " + str(final_row)
        part1 = MIMEText(
            Environment().from_string(html).render(
                {'placeholder': placeholder_lines, 'path': path}
            ), "plain"
        )
        part2 = MIMEText(
            Environment().from_string(html).render(
                {'placeholder': placeholder_lines, 'path': path}
            ), "html"
        )

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string()
            )
