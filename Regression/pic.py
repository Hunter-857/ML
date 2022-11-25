import numpy as np
import matplotlib.pyplot as plt


# x = np.arange(0, 5)
# y = 50 * x
# # # 绘制1
# plt.plot(x, y, 'r-')
# plt.legend(loc='lower right')
# plt.xlabel(xlabel="time/h")
# plt.ylabel(ylabel="distance/km")
# plt.xlim((0, 5))
# plt.ylim((0, 250))
# plt.grid()
# plt.show()
# plt.savefig("speed.png")

import requests as re
import scipy.stats as stats

rv = stats.poisson_gen()
headers = {
    "Referer": "http://photo.renren.com/photo/377471347/album-817491553/v7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
url_list = [
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w173h230q85lt_large_7LUH_673400010da61260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_nK6h_677000010d331260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w173h230q85lt_large_U0p6_677900010d4a1260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_fyGg_67de00010d031260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_rrtN_66ce00010d291260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_t6XB_66d700010d581260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w173h230q85lt_large_hRhf_66ff00010d1c1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_UGPw_66bc00010da61260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_0XM1_66c500010e0b1260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_EMij_66e000010d5b1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_ecOm_674300010e681260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_r2jc_66c500010e0c1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w173h230q85lt_large_Ca1K_66ff00010d1e1260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1630/p/m3w173h230q85lt_large_DCci_674300010e691260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_37lf_66d700010d5b1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_kjqO_67ca00010daf1260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_frcF_671c00010e231260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1630/p/m3w173h230q85lt_large_LFvq_67de00010d061260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w173h230q85lt_large_jnKD_66b300010e0c1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w173h230q85lt_large_V9fL_674e00010d891260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_91HP_67de00010d071260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w173h230q85lt_large_E7RZ_67d500010dcb1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w173h230q85lt_large_PzXB_6607000025fc1260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1630/p/m3w173h230q85lt_large_tMt5_66ff00010d201260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_x1JN_66bc00010daa1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w173h230q85lt_large_obuB_679900010de01260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_PU1I_67b500010dfa1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_qtsN_674e00010d8b1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w305h230q85lt_large_CITS_677000010d381260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_O2HF_675d00010deb1260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1630/p/m3w173h230q85lt_large_kujp_66b300010e0f1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w173h230q85lt_large_QZMa_674300010e6d1260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w173h230q85lt_large_x8rm_677900010d4f1260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w173h230q85lt_large_Fggy_67ca00010db21260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w173h230q85lt_large_nbER_674e00010d8d1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w173h230q85lt_large_ID5e_674300010e6e1260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1630/p/m3w173h230q85lt_large_dhgn_67d500010dcd1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w173h230q85lt_large_v9X5_670d00010d0c1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w173h230q85lt_large_4Ffw_67a200010db51260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w172h230q85lt_large_1K4r_67d500010dce1260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1630/p/m3w306h230q85lt_large_mx2C_671c00010e2e1260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w306h230q85lt_large_6Gg0_679900010de61260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w306h230q85lt_large_qrzf_66e000010d661260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w306h230q85lt_large_yX20_673400010db31260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w306h230q85lt_large_dZYR_67b500010e031260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w306h230q85lt_large_9WvR_672b00010d4c1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w306h230q85lt_large_72zQ_66ce00010d3a1260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1630/p/m3w306h230q85lt_large_aoB4_675d00010df61260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w306h230q85lt_large_IUlp_66c500010e1a1260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1630/p/m3w306h230q85lt_large_Uhv4_677000010d3f1260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1630/p/m3w306h230q85lt_large_CGSC_672b00010d4d1260.jpg",
"http://fmn.xnpic.com/fmn056/20120916/1630/p/m3w306h230q85lt_large_uRMN_66b300010e181260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1630/p/m3w306h230q85lt_large_ueIf_67b500010e051260.jpg",
"http://fmn.xnpic.com/fmn056/20120916/1630/p/m3w306h230q85lt_large_0rvu_66e000010d691260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1630/p/m3w306h230q85lt_large_mICa_6607000026091260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1630/p/m3w306h230q85lt_large_CiKX_66f500010d271260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w306h230q85lt_large_u4yg_670d00010d141260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w306h230q85lt_large_9PZS_673400010db61260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1630/p/m3w306h230q85lt_large_BLOt_66e000010d6a1260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1630/p/m3w306h230q85lt_large_V4Ml_66bc00010db11260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w306h230q85lt_large_VYyF_67de00010d131260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1630/p/m3w306h230q85lt_large_wPPI_67b500010e071260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w306h230q85lt_large_pGrZ_66ce00010d3e1260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1630/p/m3w306h230q85lt_large_bT1f_66b300010e1b1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w306h230q85lt_large_ke8f_674300010e7c1260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1630/p/m3w306h230q85lt_large_USXN_66d700010d6b1260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1630/p/m3w306h230q85lt_large_5sgx_674e00010d9b1260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1630/p/m3w306h230q85lt_large_7MCe_67b500010e091260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1635/p/m3w306h230q85lt_large_sxVv_67a200010dc11260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1635/p/m3w306h230q85lt_large_CLef_67de00010d161260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1635/p/m3w306h230q85lt_large_W2qV_675d00010dfb1260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1635/p/m3w306h230q85lt_large_RSk2_673400010dba1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1635/p/m3w306h230q85lt_large_05M9_675d00010dfc1260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1635/p/m3w306h230q85lt_large_0D71_677000010d461260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1635/p/m3w306h230q85lt_large_HePd_67ca00010dc01260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1635/p/m3w306h230q85lt_large_ebCv_66bc00010db61260.jpg",
"http://fmn.xnpic.com/fmn056/20120916/1635/p/m3w306h230q85lt_large_U06H_677000010d481260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1635/p/m3w306h230q85lt_large_Q4kq_677900010d621260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1635/p/m3w306h230q85lt_large_CsRy_67ca00010dc21260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1635/p/m3w306h230q85lt_large_uw4P_67b500010e0e1260.jpg",
"http://fmn.rrfmn.com/fmn061/20120916/1635/p/m3w306h230q85lt_large_z8mo_66ff00010d331260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1635/p/m3w306h230q85lt_large_CofR_670d00010d1b1260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1635/p/m3w306h230q85lt_large_uGmd_66c500010e221260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1640/p/m3w306h230q85lt_large_dO0u_674e00010de31260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1640/p/m3w306h230q85lt_large_zta5_66c500010e641260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1640/p/m3w306h230q85lt_large_IcqU_66ce00010d821260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1640/p/m3w306h230q85lt_large_gk2m_677900010da61260.jpg",
"http://fmn.xnpic.com/fmn056/20120916/1640/p/m3w306h230q85lt_large_X1OY_66d700010dab1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1640/p/m3w306h230q85lt_large_n1Bc_6607000026531260.jpg",
"http://fmn.rrimg.com/fmn064/20120916/1640/p/m3w306h230q85lt_large_sXVu_67a200010e081260.jpg",
"http://fmn.xnpic.com/fmn056/20120916/1640/p/m3w306h230q85lt_large_8cio_66bc00010dfb1260.jpg",
"http://fmn.rrimg.com/fmn065/20120916/1640/p/m3w306h230q85lt_large_BefJ_671c00010e761260.jpg",
"http://fmn.rrfmn.com/fmn059/20120916/1640/p/m3w306h230q85lt_large_jlvy_66ce00010d841260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1640/p/m3w306h230q85lt_large_94LL_66d700010dac1260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1640/p/m3w306h230q85lt_large_LbNs_674300010ec21260.jpg",
"http://fmn.rrfmn.com/fmn058/20120916/1640/p/m3w306h230q85lt_large_5hsn_66e000010db21260.jpg",
"http://fmn.xnpic.com/fmn057/20120916/1640/p/m3w306h230q85lt_large_3aOI_67b500010e521260.jpg",
"http://fmn.rrimg.com/fmn062/20120916/1640/p/m3w306h230q85lt_large_MQ9F_673400010e001260.jpg",
"http://fmn.rrfmn.com/fmn060/20120916/1640/p/m3w306h230q85lt_large_k8J9_6607000026561260.jpg",
"http://fmn.rrimg.com/fmn063/20120916/1640/p/m3w306h230q85lt_large_8c0U_672b00010d941260.jpg",
]

for url in url_list:
    response = re.request(
        url=url,
        method='GET',
        headers=headers)
    print(response.content)
    open('/Users/hunter/Desktop/image/img'+str(url_list.index(url))+'.jpg', 'wb').write(response.content)  # 将内容写入图片
    print("done" + str(url_list.index(url)))
print("finish")