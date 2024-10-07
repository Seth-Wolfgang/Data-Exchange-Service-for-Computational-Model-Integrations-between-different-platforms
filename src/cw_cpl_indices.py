from enum import Enum


class Vars(Enum):


    """
    
    
    """

    # Atmosphere to Land
    index_a2l_latitude  = 1
    index_a2l_longitude = 2 
    index_Sa_z          = 3      # Bottom atm level height                   m
    index_Sa_u          = 4      # Bottom atm level zon wind                 m/s
    index_Sa_v          = 5      # Bottom atm level mer wind                 m/s
    index_Sa_ptem       = 6      # Bottom atm level pot temp                 K
    index_Sa_shum       = 7      # Bottom atm level spec hum                 kg/kg
    index_Sa_pbot       = 8      # Bottom atm level pressure                 Pa
    index_Sa_tbot       = 9      # Bottom atm level temp                     K
    index_Faxa_lwdn     = 10     # Downward lw heat flux                     W m-2
    index_Faxa_rainc    = 11     # prec: liquid “convective”                 mm/s
    index_Faxa_rainl    = 12     # prec: liquid “large scale”                mm/s
    index_Faxa_snowc    = 13     # prec: frozen “convective”                 mm/s
    index_Faxa_snowl    = 14     # prec: frozen “large scale”                mm/s
    index_Faxa_swndr    = 15     # sw: nir direct downward                   W m-2
    index_Faxa_swvdr    = 16     # sw: vis direct downward                   W m-2
    index_Faxa_swndf    = 17     # sw: nir diffuse downward                  W m-2
    index_Faxa_swvdf    = 18     # sw: vis diffuse downward                  W m-2
    index_Sa_co2prog    = 19     # bottom atm level prognostic co2           1e-6 mol/mol
    index_Sa_co2diag    = 20     # bottom atm level diagnostic co2           1e-6 mol/mol
    index_Faxa_bcphidry = 21     # Black Carbon hydrophilic dry deposition   kg m-2 s-1
    index_Faxa_bcphodry = 22     # Black Carbon hydrophobic dry deposition   kg m-2 s-1
    index_Faxa_bcphiwet = 23     # Black Carbon hydrophilic wet deposition   kg m-2 s-1
    index_Faxa_ocphidry = 24     # Organic Carbon hydrophilic dry deposition kg m-2 s-1
    index_Faxa_ocphodry = 25     # Organic Carbon hydrophobic dry deposition kg m-2 s-1
    index_Faxa_ocphiwet = 26     # Organic Carbon hydrophilic wet deposition kg m-2 s-1
    index_Faxa_dstwet1  = 27     # Size 1 dust – wet deposition              kg m-2 s-1
    index_Faxa_dstdry1  = 28     # Size 1 dust – dry deposition              kg m-2 s-1
    index_Faxa_dstwet2  = 29     # Size 2 dust – wet deposition              kg m-2 s-1
    index_Faxa_dstdry2  = 30     # Size 2 dust – dry deposition              kg m-2 s-1
    index_Faxa_dstwet3  = 31     # Size 3 dust – wet deposition              kg m-2 s-1
    index_Faxa_dstdry3  = 32     # Size 3 dust – dry deposition              kg m-2 s-1
    index_Faxa_dstwet4  = 33     # Size 4 dust – wet deposition              kg m-2 s-1
    index_Faxa_dstdry4  = 34     # Size 4 dust – dry deposition              kg m-2 s-1

    # Land to Atmosphere
    index_l2a_latitude  = 101
    index_l2a_longitud  = 102
    index_Sl_t          = 103    # temperature                               K
    index_Sl_tref       = 104    # 2m reference temperature                  K
    index_Sl_qref       = 105    # 2m reference specific humidity            kg/kg
    index_Sl_avsdr      = 106    # albedo: direct , visible                  1
    index_Sl_anidr      = 107    # albedo: direct , near-ir                  1
    index_Sl_avsdf      = 108    # albedo: diffuse, visible                  1
    index_Sl_anidf      = 109    # albedo: diffuse, near-ir                  1
    index_Sl_snowh      = 110    # snow height                               m
    index_Sl_u10        = 111    # 10m wind                                  m
    index_Sl_fv         = 112    # friction velocity                         m/s
    index_Sl_ram1       = 113    # aerodynamical resistance                  s/m
    index_Sl_soilw      = 114    # volumetric soil water                     m3/m3
    index_Flrl_wslake   = 115    # lake water storage                        kg m-2 s-1
    index_Fall_taux     = 116    # wind stress, zonal                        N m-2
    index_Fall_tauy     = 117    # wind stress, meridional                   N m-2
    index_Fall_lat      = 118    # latent heat flux                          W m-2 
    index_Fall_sen      = 119    # sensible heat flux                        W m-2
    index_Fall_lwup     = 120    # upward longwave heat flux                 W m-2
    index_Fall_evap     = 121    # evaporation     water flux                W m-2
    index_Fall_swnet    = 122    # heat flux     shortwave net               W m-2
    index_Fall_fco2_lnd = 123    # co2 flux                                  moles m-2 s-1
    index_Fall_flxdst1  = 124    # dust flux size bin 1                      kg m-2 s-1
    index_Fall_flxdst2  = 125    # dust flux size bin 2                      kg m-2 s-1
    index_Fall_flxdst3  = 126    # dust flux size bin 3                      kg m-2 s-1
    index_Fall_flxdst4  = 127    # dust flux size bin 4                      kg m-2 s-1
    
    # Units
    index_degree                                = 1001  # degree
    index_meter                                 = 1002  # m
    index_meter_per_second                      = 1003  # m/s
    index_kelvin_dgree                          = 1004  # K
    index_kilogram_per_kilogram                 = 1005  # kg/kg
    index_pascal                                = 1006  # Pa
    index_watt_per_square_meter                 = 1007  # W m-2
    index_millimeter_per_second                 = 1008  # mm s-1
    index_parts_per_million_by_volume           = 1009  # 1e-6 mol/mol
    index_kilogram_per_meter_squared_per_second = 1010  # kg m-2 s-1
    index_unitless                              = 1011  # 1
    index_second_per_meter                      = 1012  # s m-1
    index_cubic_meter_per_cubic_meter           = 1013  # m3 m-3
    index_newton_per_square_meter               = 1014  # N m-2
    index_moles_per_square_meter_per_second     = 1015  # moles m-2 s-1

    # model (2001~3000)
    index_EAM      = 2001
    index_ELM      = 2002
    index_MOSART   = 2003
    index_MPASO    = 2004
    index_VIC5     = 2005
    index_DHSVM    = 2006
    index_WRFhydro = 2007
 
