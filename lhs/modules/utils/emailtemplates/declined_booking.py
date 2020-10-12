head = """
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="-webkit-text-size-adjust: none;width: 100%;">

    <head style="-webkit-text-size-adjust: none;">
    <meta charset="utf-8" style="-webkit-text-size-adjust: none;"> <!-- utf-8 works for most cases -->
    <!-- <meta name="viewport" content="width=device-width"> -->
    <meta name="viewport" content="width=device-width, initial-scale=1" style="-webkit-text-size-adjust: none;">
    <meta name="x-apple-disable-message-reformatting" style="-webkit-text-size-adjust: none;">
    <meta name="format-detection" content="telephone=no" style="-webkit-text-size-adjust: none;">
    <meta name="format-detection" content="date=no" style="-webkit-text-size-adjust: none;">
    <meta name="format-detection" content="address=no" style="-webkit-text-size-adjust: none;">
    <meta name="format-detection" content="email=no" style="-webkit-text-size-adjust: none;">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" style="-webkit-text-size-adjust: none;">
    <meta http-equiv="Content-Type" content="text/html charset=UTF-8" style="-webkit-text-size-adjust: none;">
    <title style="-webkit-text-size-adjust: none;"></title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,700&display=swap" rel="stylesheet" style="-webkit-text-size-adjust: none;">
    <style style="-webkit-text-size-adjust: none;">
        * {
            -webkit-text-size-adjust: none;
        }

        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
        }

        body {
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: none;
            -ms-text-size-adjust: none;

        }

        html {
            width: 100%;
        }

        table {
            border-spacing: 0;
            border-collapse: collapse;
        }

        p {
            margin: 0;
            padding: 0
        }

        tr {
            text-align: center;
        }

        td {
            padding: 0;
        }

        .second-table {
            padding: 20px;
            /*max-width: 600px;*/
            /*width: 450px;*/
            width: 100%;
            background-color: #ffffff;
            border-radius: 2.5px;
            font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';
        }

        .second-table td {
            text-align: left;
        }


        p {
            font-size: 18px;
            font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';
        }

        .fourth-table a {
            color: #4b4b4b;
            font-size: 14px;
            font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';
            line-height: 0;
            text-decoration: none;

        }

        @media only screen and (max-width: 640px) {
            /**{
                font-size: 18px;
            }*/
            h3 {
                font-size: 22px;
            }

            p {
                font-size: 20px;
            }
            a{
                font-size: 15px;
            }

            table.wrap-table {
                width: 620px !important;
                padding: 0;
            }

            table.inner-table {
                width: 600px !important;
            }

            .second-table {
                width: 400px;
            }
        }

        @media only screen and (max-width: 480px) {
            /**{
                font-size: 18px;
            }*/
            h3 {
                font-size: 22px;
            }

            p {
                font-size: 20px;
            }
            a{
                font-size: 15px;
            }

            table.wrap-table {
                width: 460px !important;
                padding: 0;
            }

            table.inner-table {
                width: 420px !important;
            }

            .second-table {
                width: 380px;
            }
        }
    </style>
    </head>
    """

def slot_declined_session(card_name,owner_name,date,time,location,booking_id,owner_message):
    body = """
        <body style="font-family: 'Open Sans', 'Verdana', 'Arial','Tahoma';-webkit-text-size-adjust: none;margin: 0;padding: 0;-ms-text-size-adjust: none;">
        <table width="100%" border="0" class="container wrap-table" align="center" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">

        <tr style="-webkit-text-size-adjust: none;text-align: center;">
            <td width="100%" valign="top" style="-webkit-text-size-adjust: none;padding: 0;">
                <table role="presentation" width="680px" align="center" class="first-table wrap-table" style="background-image: url(http://159.65.159.131/Resonace-images/common/background_header.png);background-repeat: no-repeat;background-size: cover;background-position: 50% 50%;background-color: #584BE8;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">

                    <!-- main table -->
                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="line-height: 50px;height: 20px;-webkit-text-size-adjust: none;padding: 0;">

                        </td>
                    </tr>
                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;">
                            <table style="width: 85%;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;" class="inner-table" align="center">
                                <!-- first section table -->

                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 20px;height: 30px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td valign="middle" style="color: #ffffff;-webkit-text-size-adjust: none;padding: 0;">
                                        <img src="http://159.65.159.131/Resonace-images/common/resonance-logo.png" width="120px" style="-webkit-text-size-adjust: none;">
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 15px;height: 15px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td valign="middle" style="color: #ffffff;-webkit-text-size-adjust: none;padding: 0;">
                                        <h2 style="font-size: 24px;margin: 0;-webkit-text-size-adjust: none;">Booking Declined</h2>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 10px;height: 15px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="color: #ffffff;-webkit-text-size-adjust: none;padding: 0;">
                                        <p style="font-size: 20px;line-height: 1.63;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"> <b style="-webkit-text-size-adjust: none;">"""+owner_name+"""</b> has declined your booking request!</p>
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 25px;height: 25px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td valign="middle" style="color: #ffffff;-webkit-text-size-adjust: none;padding: 0;">
                                        <img src="http://159.65.159.131/Resonace-images/declined-booking-to-booker/graphic.png" width="120px" style="-webkit-text-size-adjust: none;">
                                    </td>
                                </tr>

                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 25px;height: 25px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">

                                    <td style="padding: 15px;-webkit-text-size-adjust: none;">
                                        <!-- SESSION DETAILS CARD -->
                                        <table class="second-table" align="center" style="border-radius: 15px !important;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;padding: 20px;width: 100%;background-color: #ffffff;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">

                                            <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                <td style="padding: 20px;-webkit-text-size-adjust: none;text-align: left;">
                                                    <table cellspacing="0" cellpadding="0" width="100%" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">

                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <h3 style="text-align: center;margin: 0;font-size: 22px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';-webkit-text-size-adjust: none;">Session Details</h3>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 20px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>

                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"><b style="-webkit-text-size-adjust: none;">"""+card_name+"""</b></p>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 10px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>

                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">

                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">
                                                                    <b style="-webkit-text-size-adjust: none;">Date: </b>"""+date+"""</p>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 10px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>

                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">

                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">
                                                                    <b style="-webkit-text-size-adjust: none;">Time: </b>"""+time+"""</p>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 10px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>
                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">
                                                                    <b style="-webkit-text-size-adjust: none;">You Booked: </b>"""+owner_name+"""</p>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 10px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>
                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">
                                                                    <b style="-webkit-text-size-adjust: none;">Location: </b>"""+location+"""</p>
                                                            </td>
                                                        </tr>
                                                        <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="height: 10px;-webkit-text-size-adjust: none;padding: 0;text-align: left;"></td>
                                                        </tr>
                                                        <tr valign="top" style="-webkit-text-size-adjust: none;text-align: center;">
                                                            <td style="-webkit-text-size-adjust: none;padding: 0;text-align: left;">
                                                                <p style="color: #4b4b4b;line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">
                                                                    <b style="-webkit-text-size-adjust: none;">Booking ID: </b>"""+booking_id+"""</p>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                        <!-- SESSION DETAILS CARD -->
                                    </td>

                                </tr>


                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 20px;height: 30px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                            </table>
                        </td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                    </tr>
                </table>

                <table role="presentation" width="680px" align="center" class="wrap-table" style="border-left: 1px solid #ECEDFD;border-right: 1px solid #ECEDFD;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">

                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="-webkit-text-size-adjust: none;padding: 0;">
                            <table align="center" class="inner-table" style="max-width: 650px;width: 100%;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;" valign="middle">

                                <div id="conditional-hide" style="-webkit-text-size-adjust: none;">
                                </div><tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 25px;height: 25px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>"""
    footer = """

                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <h3 style="font-size: 22px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';-webkit-text-size-adjust: none;">Next Steps:</h3>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 6px;height: 6px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                            </table>

                        </td>
                    </tr>
                </table>

                <table bgcolor="#f6f7ff" width="680px" class="wrap-table" align="center" valign="middle" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;">
                            <table width="600px" class="inner-table" align="center" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 25px;height: 30px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td align="center" valign="middle" style="-webkit-text-size-adjust: none;padding: 0;">
                                        <img src="http://159.65.159.131/Resonace-images/common/one.png" style="display: block;-webkit-text-size-adjust: none;" width="45px">
                                        <p style="line-height: 15px;height: 15px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"></p>
                                        <p style="line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">Tap on <b style="-webkit-text-size-adjust: none;">View cancelled & Declined Bookings</b> under <b style="-webkit-text-size-adjust: none;">Bookings</b> in the <b style="-webkit-text-size-adjust: none;">Engagements</b> tab to see full details about the declined session.</p>
                                        <p style="line-height: 15px;height: 15px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"></p>
                                        <img src="http://159.65.159.131/Resonace-images/declined-booking-to-booker/mockup1.png" style="display: block;max-width: 320px;-webkit-text-size-adjust: none;" width="100%">
                                    </td>
                                </tr>
                            </table>
                        </td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                    </tr>

                </table>


                <table width="680px" class="wrap-table" align="center" style="border-left: 1px solid #ECEDFD;border-right: 1px solid #ECEDFD;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;">
                            <table class="inner-table" style="max-width: 600px;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;" align="center">
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 30px;height: 30px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <p style="line-height: 1.71;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">We’re sorry this booking didn’t work out.  Don’t hesitate to book again soon!</p>

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 30px;height: 30px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                            </table>
                        </td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                    </tr>
                </table>
                <!-- COMMON FOOTER -->
                <table class="fourth-table wrap-table" align="center" width="680px" bgcolor="#f6f7ff" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                    <tr style="-webkit-text-size-adjust: none;text-align: center;">
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;">
                            <table align="center" class="inner-table" style="max-width: 600px;-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 9px;height: 9px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <h3 style="font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';-webkit-text-size-adjust: none;">Thank you for using Resonance. Keep making art your reality!</h3>
                                        <p style="-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"> - The Resonance Team</p>
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 15px;height: 20px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="border-bottom: solid 0.5px #dcdde2;-webkit-text-size-adjust: none;padding: 0;">
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="line-height: 15px;height: 20px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <p style="line-height: 1.67;font-size: 16px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">If you ever have any questions
                                            about our
                                            platform, including building
                                            your profile, sending offers, negotiating contracts, using your schedule, or
                                            any other
                                            features don’t hesitate to email us at <a style="color: #5953eb;line-height: 1.67;font-size: 16px;-webkit-text-size-adjust: none;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';text-decoration: none;" href="#">support@yourresonance.com.</a></p>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 20px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <img src="http://159.65.159.131/Resonace-images/common/divider-line.png" style="-webkit-text-size-adjust: none;">
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 15px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <h3 style="font-size: 16px;font-weight: 600;margin: 0;-webkit-text-size-adjust: none;">We are social, drop us a
                                            line</h3>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 15px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <table cellspacing="5" align="center" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                            <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="http://www.twitter.com/ResonanceInArt" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;"><img src="http://159.65.159.131/Resonace-images/common/twitter-logo.png" width="35px" style="-webkit-text-size-adjust: none;"></a>
                                                </td>
                                                <td width="20px" style="-webkit-text-size-adjust: none;padding: 0;"></td>
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="https://instagram.com/yourresonance" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;"><img src="http://159.65.159.131/Resonace-images/common/instagram-logo.png" width="35px" style="-webkit-text-size-adjust: none;"></a>
                                                </td>
                                                <td width="20px" style="-webkit-text-size-adjust: none;padding: 0;"></td>
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="https://www.facebook.com/YourResonance/" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;"><img src="http://159.65.159.131/Resonace-images/common/facebook-logo.png" width="35px" style="-webkit-text-size-adjust: none;"></a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 20px;line-height: 20px;-webkit-text-size-adjust: none;padding: 0;">

                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <table align="center" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                            <tr valign="middle" style="-webkit-text-size-adjust: none;text-align: center;">
                                                <td valign="middle" align="center" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="#" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;">Resonance</a>
                                                </td>
                                                <td width="30px" align="center" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    |
                                                </td>
                                                <td valign="middle" align="center" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="#" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;">How it works</a>
                                                </td>
                                                <td width="30px" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    |
                                                </td>
                                                <td valign="middle" align="center" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="#" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;">FAQs</a>
                                                </td>
                                                <td width="30px" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    |
                                                </td>
                                                <td valign="middle" align="center" style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <a href="#" style="-webkit-text-size-adjust: none;color: #4b4b4b;font-size: 14px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';line-height: 0;text-decoration: none;">T&Cs</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 20px;line-height: 20px;-webkit-text-size-adjust: none;padding: 0;"></td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="-webkit-text-size-adjust: none;padding: 0;">
                                        <table align="center" style="-webkit-text-size-adjust: none;border-spacing: 0;border-collapse: collapse;">
                                            <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <img src="http://159.65.159.131/Resonace-images/common/app_store_button.png" width="125x" style="-webkit-text-size-adjust: none;">
                                                </td>
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    &nbsp;&nbsp;
                                                </td>
                                                <td style="-webkit-text-size-adjust: none;padding: 0;">
                                                    <img src="http://159.65.159.131/Resonace-images/common/google_play_button.png" width="125px" style="-webkit-text-size-adjust: none;">
                                                </td>

                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 20px;-webkit-text-size-adjust: none;padding: 0;">
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="border-bottom: solid 0.5px #dcdde2;-webkit-text-size-adjust: none;padding: 0;">
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 20px;-webkit-text-size-adjust: none;padding: 0;">
                                    </td>

                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="font-size: 12px;-webkit-text-size-adjust: none;padding: 0;">
                                        <p style="font-size: 12px;line-height: 1.5;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">You have received this email as a
                                            registered user of Resonance App.</p>
                                        <p style="line-height: 1.7;height: 2px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"></p>
                                        <p style="height: 14px;line-height: 10px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"></p>
                                        <h3 style="margin: 0;font-size: 14px;line-height: 1.5;-webkit-text-size-adjust: none;">Resonance Network Company
                                        </h3>
                                        <p style="font-size: 14px;line-height: 1.5;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">J&zwnj;ersey City, New Jersey, NY 07030 |
                                            All Rights Reserved © 2020</p>
                                    </td>
                                </tr>
                                <tr style="-webkit-text-size-adjust: none;text-align: center;">
                                    <td style="height: 25px;-webkit-text-size-adjust: none;padding: 0;">
                                    </td>

                                </tr>
                            </table>
                        </td>
                        <td style="-webkit-text-size-adjust: none;padding: 0;"></td>
                    </tr>
                </table>
                <!-- COMMON FOOTER -->
            </td>
        </tr><tr style="-webkit-text-size-adjust: none;text-align: center;">
            <td style="line-height: 50px;height: 50px;-webkit-text-size-adjust: none;padding: 0;">

            </td>
        </tr>
    </table>




    </body>

    </html>
    """
    if owner_message:
        return head + body + """<tr style="-webkit-text-size-adjust: none;text-align: center;">

            <td align="center" valign="middle" style="-webkit-text-size-adjust: none;padding: 0;">
                <h3 style="margin: 0;font-size: 22px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';-webkit-text-size-adjust: none;">Message from """+owner_name+"""</h3>
                <img src="http://159.65.159.131/Resonace-images/common/underline.png" width="120px" style="-webkit-text-size-adjust: none;">
                <p style="line-height: 15px;height: 15px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-size: 18px;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';"></p>
                <p style="font-size: 18px;-webkit-text-size-adjust: none;margin: 0;padding: 0;font-family: 'Open Sans', 'Verdana', 'Arial', 'Tahoma';">"""+owner_message+"""</p>
            </td>

        </tr>
        <tr style="-webkit-text-size-adjust: none;text-align: center;">
            <td style="line-height: 20px;height: 20px;-webkit-text-size-adjust: none;padding: 0;">

            </td>
        </tr>


        <tr style="-webkit-text-size-adjust: none;text-align: center;">
            <td style="border-bottom: solid 0.5px #dcdde2;-webkit-text-size-adjust: none;padding: 0;">
            </td>

        </tr>
        <tr style="-webkit-text-size-adjust: none;text-align: center;">
            <td style="line-height: 8px;height: 8px;-webkit-text-size-adjust: none;padding: 0;">

            </td>
        </tr> """+footer
    else:

        return head+body+footer
