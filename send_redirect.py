@staticmethod
    def send_direct_email(conid, support_eamil_addr, title, content, downpdf_conid=-1, downpdf_docid=-1, downpdf_tenantid=-1, **params):
        """
        이 함수는 서포트 이메일로 수신 시 발생하는 base64 디코딩을 해결하는 함수입니다.
        """
        mylogger.info("==== send_direct_email  진입 ====")
        company_name = params['company']
        support_content = content
        user_email = params['request_email']
        mylogger.info(" 123123 {},{},{}".format(params['request_email'], params['request_employee_no'], params['request_admin']))

        img_src_list = []
        soup = BeautifulSoup(support_content, 'html.parser')
        for img_src in soup.find_all("img"):
            img_src_list.append(img_src["src"].split('base64,')[1])
            soup.img['src'] = 0
            soup.img.decompose()

        str(soup)

        directory = '/userdata/temp/support/'

        # 디렉토리가 없는 경우 생성.
        FileUtils.mkdir_if_not_exists(directory)

        # 디렉토리 생성됨
        attachement_list = []
        for i in range(len(img_src_list)):
            filename = directory + datetime.now().strftime("%Y%m%d-%H%M") + ' - ' + user_email.split('@')[0] + str(i) + '.jpg'
            img_data = base64.b64decode(img_src_list[i])
            with open(filename, 'wb') as f:
                f.write(img_data)
                attachement_list.append(filename)

        # mail = Mail(Email(user_email, company_name), title,
        #             Email(support_eamil_addr), Content("text/html", str(soup)))
        attachment = Attachment()
        try:
            for one in attachement_list:
                with open(one, 'rb') as input_fp:
                    input_fp.seek(0)
                    # attachment = Attachment()
                    attachment.type = "application/jpg"
                    filename, file_extension = os.path.splitext(one)
                    attachment.filename = filename + file_extension
                    attachment.content = base64.b64encode(input_fp.read()).decode()
                    # mail.add_attachment(attachment)

        except Exception as e:
            mylogger.info("==== base64 decode ERROR ====")

        # for one_base64_str in img_src_list:
        #     # 생성된 pdf 파일을 첨부파일로 attach 한다.
        #     attachment = Attachment()
        #     attachment.type = "application/jpg"
        #     one_base64_byte = base64.b64decode(one_base64_str)
        #     attachment.filename = "test.jpg"
        #     attachment.content = base64.b64encode(one_base64_byte).decode()
        #     mail.add_attachment(attachment)

        # sg = sendgrid.SendGridAPIClient(apikey=CONS.SENDGRID_APIKEY)
        # sg.client.mail.send.post(request_body=mail.get())
