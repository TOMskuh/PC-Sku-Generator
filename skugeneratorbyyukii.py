def generate_xml(codenames):
    xml_template = '''<?xml version="1.0" encoding="utf-8"?>
<root>
    <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="skuscene_db" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/skuscenes/skuscene_base.tpl">
                <COMPONENTS NAME="JD_SongDatabaseComponent">
                    <JD_SongDatabaseComponent></JD_SongDatabaseComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        '''
    
    for codename in codenames:
        xml_template += f'''
        <ACTORS NAME="Actor">
            <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{codename}" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/{codename}/songdesc.tpl">
                <COMPONENTS NAME="JD_SongDescComponent">
                    <JD_SongDescComponent></JD_SongDescComponent>
                </COMPONENTS>
            </Actor>
        </ACTORS>
        '''
    
    xml_template += '''
        <sceneConfigs>
            <SceneConfigs activeSceneConfig="0">
                <sceneConfigs NAME="JD_SongDatabaseSceneConfig">
                    <JD_SongDatabaseSceneConfig name="" SKU="jd2017-pc-ww" Territory="NCSA" RatingUI="world/ui/screens/bootsequence/rating">
                        <ENUM NAME="Pause_Level" SEL="6"></ENUM>
        '''
    
    for codename in codenames:
        xml_template += f'''
                        <CoverflowSkuSongs>
                            <CoverflowSong name="{codename}" cover_path="world/maps/{codename}/menuart/actors/{codename}_cover_online.act"></CoverflowSong>
                        </CoverflowSkuSongs>
        '''
    
    xml_template += '''
                    </JD_SongDatabaseSceneConfig>
                </sceneConfigs>
            </SceneConfigs>
        </sceneConfigs>
    </Scene>
</root>
'''
    return xml_template

print("Hello! Welcome to the PC SKU Gen made by Yukii.")
codenames_input = input("Please enter the codenames separated by commas (e.g., codename1, codename2, codename3): ")
codenames_array = [codename.strip() for codename in codenames_input.split(',')]
generated_xml = generate_xml(codenames_array)

output_filename = "skuscene_maps_pc_all.isc.ckd"
with open(output_filename, "w") as output_file:
    output_file.write(generated_xml)

print(f"SKU succesfully generated in {output_filename}! Thank you for using our tool!")
