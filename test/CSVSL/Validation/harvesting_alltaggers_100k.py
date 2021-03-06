import FWCore.ParameterSet.Config as cms

process = cms.Process("harvesting")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EDMtoMEAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger.cerr.threshold = 'ERROR'

# for the conditions
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['startup']

# Open and read list file
#filename = open('RootFiles/list.list', 'r')
#filelist = cms.untracked.vstring( filename.readlines() )

# Input source
process.source = cms.Source("PoolSource",
  #fileNames = filelist,
  fileNames = cms.untracked.vstring(),
  secondaryFileNames = cms.untracked.vstring(),
  processingMode = cms.untracked.string('RunsAndLumis')
)


process.options = cms.untracked.PSet(
  Rethrow = cms.untracked.vstring('ProductNotFound'),
  fileMode = cms.untracked.string('FULLMERGE')
)

from DQMOffline.RecoB.bTagCommon_cff import*
process.load("DQMOffline.RecoB.bTagCommon_cff")
#process.bTagCommonBlock.ptRecJetMin = cms.double(600.0)
process.bTagCommonBlock.ptRanges = cms.vdouble(0.0,40.0,60.0,90.0, 150.0,400.0,600.0,3000.0)
process.bTagCommonBlock.etaRanges = cms.vdouble(0.0, 1.2, 2.1, 2.4)

###############################################################################################

from Validation.RecoB.bTagAnalysis_cfi import *
process.load("Validation.RecoB.bTagAnalysis_cfi")

process.CustombTagValidation = process.bTagValidation.clone(
    tagConfig = cms.VPSet(
				cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("trackCountingHighEffBJetTags"),
            folder = cms.string("TCHE")
        ), 
        cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("trackCountingHighPurBJetTags"),
            folder = cms.string("TCHP")
        ), 
        cms.PSet(
            bTagProbabilityAnalysisBlock,
            label = cms.InputTag("jetProbabilityBJetTags"),
            folder = cms.string("JP")
        ), 
        cms.PSet(
            bTagBProbabilityAnalysisBlock,
            label = cms.InputTag("jetBProbabilityBJetTags"),
            folder = cms.string("JBP")
        ), 
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("simpleSecondaryVertexHighEffBJetTags"),
            folder = cms.string("SSVHE")
        ), 
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("simpleSecondaryVertexHighPurBJetTags"),
            folder = cms.string("SSVHP")
        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexBJetTags"),
            folder = cms.string("oldCSV") # standard CSV for 7 TeV data taking
        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexV1BJetTags"),
            folder = cms.string("CSVV1") # LR-based CSV
        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexV2BJetTags"),
            folder = cms.string("CSVV2") # MLP-based CSV
        ),
#				cms.PSet(
#				    parameters = cms.PSet(
#        			discriminatorStart = cms.double(-0.1),
#        			discriminatorEnd = cms.double(1.05),
#        			nBinEffPur = cms.int32(200),
#        			# the constant b-efficiency for the differential plots versus pt and eta
#        			effBConst = cms.double(0.5),
#        			endEffPur = cms.double(1.005),
#        			startEffPur = cms.double(-0.005)
#    				),
#            label = cms.InputTag("combinedSecondaryVertexSoftLeptonBJetTags"),
#            folder = cms.string("CSVSL") # CSVSL
#        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexIVFBJetTags"),
            folder = cms.string("oldCSVIVF") # standard CSV+IVF for 7 TeV data taking
        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexIVFV1BJetTags"),
            folder = cms.string("CSVIVFV1") # LR+IVF-based CSV
        ), 
        cms.PSet(
				    parameters = cms.PSet(
        			discriminatorStart = cms.double(-0.1),
        			discriminatorEnd = cms.double(1.05),
        			nBinEffPur = cms.int32(200),
        			# the constant b-efficiency for the differential plots versus pt and eta
        			effBConst = cms.double(0.5),
        			endEffPur = cms.double(1.005),
        			startEffPur = cms.double(-0.005)
    				),
            label = cms.InputTag("combinedSecondaryVertexIVFV2BJetTags"),
            folder = cms.string("CSVIVFV2") # MLP+IVF-based CSV
        )#,
#				cms.PSet(
#				    parameters = cms.PSet(
#        			discriminatorStart = cms.double(-0.1),
#        			discriminatorEnd = cms.double(1.05),
#        			nBinEffPur = cms.int32(200),
#        			# the constant b-efficiency for the differential plots versus pt and eta
#        			effBConst = cms.double(0.5),
#        			endEffPur = cms.double(1.005),
#        			startEffPur = cms.double(-0.005)
#    				),
#            label = cms.InputTag("combinedSecondaryVertexSoftLeptonIVFBJetTags"),
#            folder = cms.string("CSVIVFSL") # IVF-based CSVSL
#        ) 
			)
)

process.dqmEnv.subSystemFolder = 'BTAG'
process.dqmSaver.producer = 'DQM'
#process.dqmSaver.workflow = '/POG/BTAG/BJETtrained20k_eachptetabin_NewTrackSelection_modified16_tighttracksel'
process.dqmSaver.workflow = '/POG/BTAG/all'
process.dqmSaver.convention = 'Offline'
process.dqmSaver.saveByRun = cms.untracked.int32(-1)
process.dqmSaver.saveAtJobEnd =cms.untracked.bool(True)
process.dqmSaver.forceRunNumber = cms.untracked.int32(1)

# Path and EndPath definitions
process.edmtome_step = cms.Path(process.EDMtoME)
process.bTagValidation_step = cms.Path(process.CustombTagValidation)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(
  process.edmtome_step,
  process.bTagValidation_step,
  process.dqmsave_step
)

process.PoolSource.fileNames = [
#'/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_100_1_ZIR.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_101_1_lBI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_102_1_Xkq.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_103_1_ZxQ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_104_1_IHp.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_105_1_SK4.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_106_1_VbS.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_107_1_TcC.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_108_1_paM.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_109_1_IqQ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_10_1_fxN.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_110_1_glB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_111_1_U3x.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_112_1_IGe.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_113_1_sBK.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_114_1_Zm3.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_115_1_sMB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_116_1_fYQ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_117_1_C0A.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_118_1_pKE.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_119_1_B5F.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_11_1_2Yu.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_120_1_Rft.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_121_1_6Ix.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_122_1_gjZ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_123_1_eXA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_124_1_QzE.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_125_1_IRH.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_126_1_F6W.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_127_1_UhW.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_128_1_zeF.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_129_1_nDk.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_12_1_cCI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_130_1_K6T.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_131_1_8lA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_132_1_78i.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_135_1_CBP.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_136_1_Q1y.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_137_1_o1B.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_138_1_GFG.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_139_1_XeV.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_13_1_8Uv.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_140_1_8GN.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_141_1_YCI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_142_1_9vh.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_143_1_5bM.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_144_1_1sL.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_145_1_0Dk.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_146_1_c8x.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_147_1_s9K.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_148_1_Sgm.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_149_1_aA2.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_14_1_vs5.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_150_1_5Sg.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_151_1_EBg.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_152_1_KUP.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_153_1_e96.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_154_1_GFJ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_155_1_dgS.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_156_1_PqB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_157_1_T9x.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_158_1_8Az.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_159_1_anx.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_15_1_jqx.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_160_1_oCi.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_161_1_7a2.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_162_1_bPn.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_163_1_4oA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_164_1_PrT.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_165_1_hMz.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_166_1_dKp.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_167_1_Unm.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_168_1_Be7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_169_1_V7k.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_16_1_nn8.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_170_1_DcP.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_171_1_ou3.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_172_1_eiO.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_173_1_i5o.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_174_1_S1t.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_175_1_QCE.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_176_1_jpv.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_177_1_05h.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_178_1_Eom.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_179_1_X2i.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_17_1_Piw.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_180_1_xkj.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_181_1_IEj.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_182_1_xhz.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_183_1_uwf.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_184_1_ETY.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_185_1_dAe.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_186_1_ECs.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_187_1_y8L.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_188_1_NQM.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_189_1_a5q.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_18_1_nTF.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_190_1_IZi.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_191_1_YUG.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_192_1_pt7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_193_1_E9U.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_194_1_HXf.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_195_1_lXB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_196_1_y7i.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_197_1_xbn.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_198_1_KtR.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_199_1_A0P.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_19_1_E5m.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_1_1_Mjk.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_200_1_oTH.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_201_1_lEu.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_202_1_Vuf.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_203_1_NV1.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_204_1_LvG.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_205_1_Wps.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_206_1_a5B.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_207_1_F2M.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_208_1_zfF.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_209_1_7xI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_20_1_BVF.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_210_1_5DD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_211_1_rp8.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_212_1_8bS.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_213_1_kxW.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_214_1_FIt.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_215_1_EsO.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_216_1_qhX.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_217_1_GNK.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_218_1_61i.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_219_1_FW1.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_21_1_3g6.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_220_1_M6Q.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_221_1_e2j.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_222_1_nUS.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_223_1_mll.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_224_1_Pzk.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_225_1_mTN.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_226_1_nif.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_227_1_MQe.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_228_1_lkf.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_229_1_m0x.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_22_1_iFA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_230_1_JyI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_231_1_Cip.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_232_1_uzK.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_233_1_zCs.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_234_1_TPr.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_235_1_L9s.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_236_1_xZ1.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_237_1_opy.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_238_1_nLq.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_239_1_UlL.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_23_1_N8X.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_240_1_0fh.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_241_1_D6q.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_242_1_XHs.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_243_1_xeR.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_244_1_rdo.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_245_1_7bJ.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_246_1_285.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_247_1_ozB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_248_1_EmB.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_249_1_T97.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_24_1_FDD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_250_1_W6p.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_25_1_4nx.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_26_1_fCe.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_27_1_Fh2.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_28_1_rvk.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_29_1_xdR.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_2_1_XAA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_30_1_G5x.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_31_1_PoG.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_32_1_dEl.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_33_1_N1v.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_34_1_nQT.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_35_1_dcD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_36_1_vLR.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_37_1_vXj.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_38_1_9h7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_39_1_nO1.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_3_1_l1b.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_40_1_CQm.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_41_1_HX2.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_42_1_05g.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_43_1_R4m.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_44_1_8Zc.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_45_1_jfj.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_46_1_una.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_47_1_VrY.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_48_1_QEr.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_49_1_FLx.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_4_1_noI.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_50_1_p18.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_51_1_qCO.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_52_1_t7B.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_53_1_o1P.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_54_1_W77.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_55_1_cme.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_56_1_xu7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_57_1_qax.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_58_1_XH3.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_59_1_7OD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_5_1_JOh.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_60_1_1As.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_61_1_gih.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_62_1_UeV.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_63_1_sVT.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_64_1_i6A.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_65_1_JnD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_66_1_4Wz.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_67_1_Pdi.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_68_1_00S.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_69_1_hRh.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_6_1_vUu.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_70_1_APH.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_71_1_7ah.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_72_1_XlU.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_73_1_5C7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_74_1_6Tm.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_75_1_cWj.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_76_1_33G.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_77_1_v0Z.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_78_1_ID7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_79_1_8UU.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_7_1_2yi.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_80_1_MQL.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_81_1_Ak6.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_82_1_ZH3.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_83_1_VY5.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_84_1_QcP.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_85_1_H1t.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_86_1_LSr.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_87_1_Lxw.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_88_1_1Si.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_89_1_QRD.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_8_1_YCh.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_90_1_5t7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_91_1_bcA.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_92_1_9M7.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_93_1_V97.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_94_1_Hf5.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_95_1_tIE.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_96_1_ek6.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_97_1_x97.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_98_1_E1J.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_99_1_9ay.root', '/store/user/pvmulder/BtagValidation_5314/myCSVSL_20142402_minIPsig/DQMfile_9_1_mLc.root'
'file:DQMfile.root'
]
