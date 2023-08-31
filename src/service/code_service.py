from src.dao.code_dao import codeDao


class CodeService:


    def create_code(self, code_name, exec_txt, accounts_exp_1, accounts_exp_2, proxy_ip_exp, param_exp, code_desc):
        records = []
        records.append((code_name, exec_txt, accounts_exp_1, accounts_exp_2, proxy_ip_exp, param_exp, code_desc))
        codeDao.insert_batch(records)

    def modify_code(self, msg_dict):
        codeDao.update_by_id(msg_dict)


    def query_code_by_name(self, code_name):
        return codeDao.select_by_name(code_name)



codeService = CodeService()

if __name__ == '__main__':
    c = CodeService()

    print('')

    print('finish.....')