#!/usr/bin/env python

#
#############################################################################
#
# mtpdef - Media Transfer Protocol definitions
# Copyright (C) 2015, testcams.com
#
# This module is licensed under GPL v3: http://www.gnu.org/licenses/gpl-3.0.html
#
#############################################################################
#

from __future__ import print_function
from __future__ import division
from collections import namedtuple

#
# MTP Operation Codes
#
MTP_OP_GetDeviceInfo 			= 0x1001
MTP_OP_OpenSession 				= 0x1002
MTP_OP_CloseSession				= 0x1003
MTP_OP_GetStorageIDs			= 0x1004
MTP_OP_GetStorageInfo			= 0x1005
MTP_OP_GetNumObjects			= 0x1006
MTP_OP_GetObjectHandles			= 0x1007
MTP_OP_GetObjectInfo			= 0x1008
MTP_OP_GetObject				= 0x1009
MTP_OP_GetThumb					= 0x100a
MTP_OP_DeleteObject				= 0x100b
MTP_OP_SendObjectInfo			= 0x100c
MTP_OP_SendObject				= 0x100d
MTP_OP_InitiateCapture			= 0x100e
MTP_OP_FormatStore				= 0x100f
MTP_OP_GetDevicePropDesc		= 0x1014
MTP_OP_GetDevicePropValue		= 0x1015
MTP_OP_SetDevicePropValue		= 0x1016
MTP_OP_GetPartialObject			= 0x101b
MTP_OP_InitiateCaptureRecInSdram =0x90c0
MTP_OP_AfDrive					= 0x90c1
MTP_OP_ChangeCameraMode			= 0x90c2
MTP_OP_DeleteImagesInSdram		= 0x90c3
MTP_OP_GetLargeThumb			= 0x90c4
MTP_OP_GetEvent					= 0x90c7
MTP_OP_DeviceReady				= 0x90c8
MTP_OP_SetPreWbData				= 0x90c9
MTP_OP_GetVendorPropCodes		= 0x90ca
MTP_OP_AfAndCaptureRecInSdram 	= 0x90cb
MTP_OP_GetPicCtrlData			= 0x90cc
MTP_OP_SetPicCtrlData			= 0x90cd
MTP_OP_DeleteCustomPicCtrl		= 0x90ce
MTP_OP_GetPicCtrlCapability		= 0x90cf
MTP_OP_StartLiveView			= 0x9201
MTP_OP_EndLiveView				= 0x9202
MTP_OP_GetLiveViewImage			= 0x9203
MTP_OP_MfDrive					= 0x9204
MTP_OP_ChangeAfArea				= 0x9205
MTP_OP_AfDriveCancel			= 0x9206
MTP_OP_InitiateCatureRecInMedia = 0x9207
MTP_OP_GetVendorStorageIDs		= 0x9209
MTP_OP_StartMovieRecInCard		= 0x920a
MTP_OP_EndMovieRec				= 0x920b
MTP_OP_TerminateCapture			= 0x920c
MTP_OP_GetPartialOjectHighSpeed = 0x9400
MTP_OP_StartSpotWb				= 0x9402
MTP_OP_EndSpotWb				= 0x9403
MTP_OP_ChangeSpotWbArea			= 0x9404
MTP_OP_MeasureSpotWb			= 0x9405
MTP_OP_EndSpotWbResultDisp  	= 0x9406
MTP_OP_SetTransferListLock  	= 0x9407
MTP_OP_GetTransferList			= 0x9408
MTP_OP_NotifyFileAcquisitionStart =0x9409
MTP_OP_NotifyFileAcquisitionEnd = 0x940a
MTP_OP_GetSpecificSizeObject	= 0x940b
MTP_OP_CancelImagesInSdram		= 0x940c
MTP_OP_GetPicCtrlDataEx			= 0x940d
MTP_OP_SetPicCtrlDataEx			= 0x940e
MTP_OP_DeleteMovieCustomPicCtrl = 0x940f
MTP_OP_GetMoviePicCtrlCapability= 0x9410
MTP_OP_GetObjectProprsSupported = 0x9801
MTP_OP_GetObjectPropDesc		= 0x9802
MTP_OP_GetObjectPropValue		= 0x9803
MTP_OP_GetObjectPropList		= 0x9805

MtpOpDescDictionary = {\
	MTP_OP_GetDeviceInfo 			: 'MTP_OP_GetDeviceInfo',
	MTP_OP_OpenSession 				: 'MTP_OP_OpenSession',
	MTP_OP_CloseSession				: 'MTP_OP_CloseSession',
	MTP_OP_GetStorageIDs			: 'MTP_OP_GetStorageIDs',
	MTP_OP_GetStorageInfo			: 'MTP_OP_GetStorageInfo',
	MTP_OP_GetNumObjects			: 'MTP_OP_GetNumObjects',
	MTP_OP_GetObjectHandles			: 'MTP_OP_GetObjectHandles',
	MTP_OP_GetObjectInfo			: 'MTP_OP_GetObjectInfo',
	MTP_OP_GetObject				: 'MTP_OP_GetObject',
	MTP_OP_GetThumb					: 'MTP_OP_GetThumb',
	MTP_OP_DeleteObject				: 'MTP_OP_DeleteObject',
	MTP_OP_SendObjectInfo			: 'MTP_OP_SendObjectInfo',
	MTP_OP_SendObject				: 'MTP_OP_SendObjectv',
	MTP_OP_InitiateCapture			: 'MTP_OP_InitiateCapture',
	MTP_OP_FormatStore				: 'MTP_OP_FormatStore',
	MTP_OP_GetDevicePropDesc		: 'MTP_OP_GetDevicePropDesc',
	MTP_OP_GetDevicePropValue		: 'MTP_OP_GetDevicePropValue',
	MTP_OP_SetDevicePropValue		: 'MTP_OP_SetDevicePropValue',
	MTP_OP_GetPartialObject			: 'MTP_OP_GetPartialObject',
	MTP_OP_InitiateCaptureRecInSdram : 'MTP_OP_InitiateCaptureRecInSdram',
	MTP_OP_AfDrive					: 'MTP_OP_AfDrive',
	MTP_OP_ChangeCameraMode			: 'MTP_OP_ChangeCameraMode',
	MTP_OP_DeleteImagesInSdram		: 'MTP_OP_DeleteImagesInSdram',
	MTP_OP_GetLargeThumb			: 'MTP_OP_GetLargeThumb',
	MTP_OP_GetEvent					: 'MTP_OP_GetEvent',
	MTP_OP_DeviceReady				: 'MTP_OP_DeviceReady',
	MTP_OP_SetPreWbData				: 'MTP_OP_SetPreWbData',
	MTP_OP_GetVendorPropCodes		: 'MTP_OP_GetVendorPropCodes',
	MTP_OP_AfAndCaptureRecInSdram 	: 'MTP_OP_AfAndCaptureRecInSdram',
	MTP_OP_GetPicCtrlData			: 'MTP_OP_GetPicCtrlData',
	MTP_OP_SetPicCtrlData			: 'MTP_OP_SetPicCtrlData',
	MTP_OP_DeleteCustomPicCtrl		: 'MTP_OP_DeleteCustomPicCtrl',
	MTP_OP_GetPicCtrlCapability		: 'MTP_OP_GetPicCtrlCapability',
	MTP_OP_StartLiveView			: 'MTP_OP_StartLiveView',
	MTP_OP_EndLiveView				: 'MTP_OP_EndLiveView',
	MTP_OP_GetLiveViewImage			: 'MTP_OP_GetLiveViewImage',
	MTP_OP_MfDrive					: 'MTP_OP_MfDrive',
	MTP_OP_ChangeAfArea				: 'MTP_OP_ChangeAfArea',
	MTP_OP_AfDriveCancel			: 'MTP_OP_AfDriveCancel',
	MTP_OP_InitiateCatureRecInMedia : 'MTP_OP_InitiateCatureRecInMedia',
	MTP_OP_GetVendorStorageIDs		: 'MTP_OP_GetVendorStorageIDs',
	MTP_OP_StartMovieRecInCard		: 'MTP_OP_StartMovieRecInCard',
	MTP_OP_EndMovieRec				: 'MTP_OP_EndMovieRec',
	MTP_OP_TerminateCapture			: 'MTP_OP_TerminateCapture',
	MTP_OP_GetPartialOjectHighSpeed : 'MTP_OP_GetPartialOjectHighSpeed',
	MTP_OP_StartSpotWb				: 'MTP_OP_StartSpotWb',
	MTP_OP_EndSpotWb				: 'MTP_OP_EndSpotWb',
	MTP_OP_ChangeSpotWbArea			: 'MTP_OP_ChangeSpotWbArea',
	MTP_OP_MeasureSpotWb			: 'MTP_OP_MeasureSpotWb',
	MTP_OP_EndSpotWbResultDisp  	: 'MTP_OP_EndSpotWbResultDisp',
	MTP_OP_SetTransferListLock  	: 'MTP_OP_SetTransferListLock',
	MTP_OP_GetTransferList			: 'MTP_OP_GetTransferList',
	MTP_OP_NotifyFileAcquisitionStart : 'MTP_OP_NotifyFileAcquisitionStart',
	MTP_OP_NotifyFileAcquisitionEnd : 'MTP_OP_NotifyFileAcquisitionEnd',
	MTP_OP_GetSpecificSizeObject	: 'MTP_OP_GetSpecificSizeObject',
	MTP_OP_CancelImagesInSdram		: 'MTP_OP_CancelImagesInSdram',
	MTP_OP_GetPicCtrlDataEx			: 'MTP_OP_GetPicCtrlDataEx',
	MTP_OP_SetPicCtrlDataEx			: 'MTP_OP_SetPicCtrlDataEx',
	MTP_OP_DeleteMovieCustomPicCtrl : 'MTP_OP_DeleteMovieCustomPicCtrl',
	MTP_OP_GetMoviePicCtrlCapability: 'MTP_OP_GetMoviePicCtrlCapability',
	MTP_OP_GetObjectProprsSupported : 'MTP_OP_GetObjectProprsSupported',
	MTP_OP_GetObjectPropDesc		: 'MTP_OP_GetObjectPropDesc',
	MTP_OP_GetObjectPropValue		: 'MTP_OP_GetObjectPropValue',
	MTP_OP_GetObjectPropList		: 'MTP_OP_GetObjectPropList'
}
def getMtpOpDesc(mtpOp):
	if mtpOp in MtpOpDescDictionary:
		return "{:s}".format(MtpOpDescDictionary[mtpOp])
	else:
		return "Unknown Op Code (0x{:04x})".format(mtpOp)

#
# not in the spec, but here are constants for the possible
# data directions of MTP commands, plus a dictonary for a
# quick lookup for the data direction for each OP
#		
MTP_DATA_DIRECTION_NONE				= 0
MTP_DATA_DIRECTION_CAMERA_TO_HOST	= 1
MTP_DATA_DIRECTION_HOST_TO_CAMERA	= 2
		
MtpOpDataDirections = {\
	MTP_OP_GetDeviceInfo 			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_OpenSession 				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_CloseSession				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetStorageIDs			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetStorageInfo			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetNumObjects			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetObjectHandles			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetObjectInfo			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetObject				: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetThumb					: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_DeleteObject				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_SendObjectInfo			: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_SendObject				: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_InitiateCapture			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_FormatStore				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetDevicePropDesc		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetDevicePropValue		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_SetDevicePropValue		: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_GetPartialObject			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_InitiateCaptureRecInSdram : MTP_DATA_DIRECTION_NONE,
	MTP_OP_AfDrive					: MTP_DATA_DIRECTION_NONE,
	MTP_OP_ChangeCameraMode			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_DeleteImagesInSdram		: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetLargeThumb			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetEvent					: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_DeviceReady				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_SetPreWbData				: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_GetVendorPropCodes		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_AfAndCaptureRecInSdram 	: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetPicCtrlData			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_SetPicCtrlData			: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_DeleteCustomPicCtrl		: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetPicCtrlCapability		: MTP_DATA_DIRECTION_NONE,
	MTP_OP_StartLiveView			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_EndLiveView				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetLiveViewImage			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_MfDrive					: MTP_DATA_DIRECTION_NONE,
	MTP_OP_ChangeAfArea				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_AfDriveCancel			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_InitiateCatureRecInMedia : MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetVendorStorageIDs		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_StartMovieRecInCard		: MTP_DATA_DIRECTION_NONE,
	MTP_OP_EndMovieRec				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_TerminateCapture			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetPartialOjectHighSpeed : MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_StartSpotWb				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_EndSpotWb				: MTP_DATA_DIRECTION_NONE,
	MTP_OP_ChangeSpotWbArea			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_MeasureSpotWb			: MTP_DATA_DIRECTION_NONE,
	MTP_OP_EndSpotWbResultDisp  	: MTP_DATA_DIRECTION_NONE,
	MTP_OP_SetTransferListLock  	: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetTransferList			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_NotifyFileAcquisitionStart : MTP_DATA_DIRECTION_NONE,
	MTP_OP_NotifyFileAcquisitionEnd : MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetSpecificSizeObject	: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_CancelImagesInSdram		: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetPicCtrlDataEx			: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_SetPicCtrlDataEx			: MTP_DATA_DIRECTION_HOST_TO_CAMERA,
	MTP_OP_DeleteMovieCustomPicCtrl : MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetMoviePicCtrlCapability: MTP_DATA_DIRECTION_NONE,
	MTP_OP_GetObjectProprsSupported : MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetObjectPropDesc		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetObjectPropValue		: MTP_DATA_DIRECTION_CAMERA_TO_HOST,
	MTP_OP_GetObjectPropList		: MTP_DATA_DIRECTION_CAMERA_TO_HOST
}
def getMtpOpDataDirection(mtpOp):
	if mtpOp in MtpOpDataDirections:
		return MtpOpDataDirections[mtpOp]
	else:
		raise AssertionError("getMtpOpDataDirection called with an op 0x{:x} that is not in MtpOpDataDirections!".format(mtpOp))


#
# MTP Response Codes
#
MTP_RESP_Ok										= 0x2001
MTP_RESP_GeneralError							= 0x2002
MTP_RESP_SessionNotOpen							= 0x2003
MTP_RESP_InvalidTransactionId					= 0x2004
MTP_RESP_OperationNotSupported					= 0x2005
MTP_RESP_ParameterNotSupported					= 0x2006
MTP_RESP_IncompleteTransfer						= 0x2007
MTP_RESP_InvalidStorageID						= 0x2008
MTP_RESP_InvalidObjectHandle					= 0x2009
MTP_RESP_DevicePropNotSupported					= 0x200a
MTP_RESP_InvalidObjectFormatCode				= 0x200b
MTP_RESP_StoreFull								= 0x200c
MTP_RESP_ObjectWriteProtect						= 0x200d
MTP_RESP_StoreReadOnly							= 0x200e
MTP_RESP_AccessDenied							= 0x200f
MTP_RESP_NoThumbnailPresent						= 0x2010
MTP_RESP_PartialDeletion						= 0x2012
MTP_RESP_StoreNotAvailable						= 0x2013
MTP_RESP_SpecificiationByFormatUnsupported		= 0x2014
MTP_RESP_NoValidObjectInfo						= 0x2015
MTP_RESP_DeviceBusy								= 0x2019
MTP_RESP_InvalidParentObject					= 0x201a
MTP_RESP_InvalidDevicePropFormat				= 0x201b
MTP_RESP_InvalidDevicePropValue					= 0x201c
MTP_RESP_InvalidParameter						= 0x201d
MTP_RESP_SessionAlreadyOpen						= 0x201e
MTP_RESP_SpecificationOfDestinationUnsupported	= 0x2020
MTP_RESP_HardwareError							= 0xa001
MTP_RESP_OutOfFocus								= 0xa002
MTP_RESP_ChangeCameraModeFailed					= 0xa003
MTP_RESP_InvalidStatus							= 0xa004
MTP_RESP_WbPresentError							= 0xa006
MTP_RESP_DustReferenceError						= 0xa007
MTP_RESP_ShutterSpeedBulb						= 0xa008
MTP_RESP_MirrorUpSequence						= 0xa009
MTP_RESP_CameraModeNotAdjustFnumber				= 0xa00a
MTP_RESP_NotLiveView							= 0xa00b
MTP_RESP_MfDriveStepEnd							= 0xa00c
MTP_RESP_MfDriveStepInsufficiency				= 0xa00e
MTP_RESP_StoreError								= 0xa021
MTP_RESP_StoreUnformatted						= 0xa022
MTP_RESP_BulbReleaseBusy						= 0xa200
MTP_RESP_ShutterSpeedTime						= 0xa204
MTP_RESP_NoTransferList							= 0xa205
MTP_RESP_NoJpegPresent							= 0xa206
MTP_RESP_InvalidObjectPropCode					= 0xa801
MTP_RESP_InvalidObjectPropFormat				= 0xa802
MTP_RESP_COMMUNICATION_ERROR					= 0xfffe	# fake response I use internally to convey error in transmitting/receiving MTP request

MtpRespDescDictionary = {\
	MTP_RESP_Ok : 'MTP_RESP_Ok',
	MTP_RESP_GeneralError : 'MTP_RESP_GeneralError',
	MTP_RESP_SessionNotOpen : 'MTP_RESP_SessionNotOpen',
	MTP_RESP_InvalidTransactionId : 'MTP_RESP_InvalidTransactionId',
	MTP_RESP_OperationNotSupported : 'MTP_RESP_OperationNotSupported',
	MTP_RESP_ParameterNotSupported : 'MTP_RESP_ParameterNotSupported',
	MTP_RESP_IncompleteTransfer : 'MTP_RESP_IncompleteTransfer',
	MTP_RESP_InvalidStorageID : 'MTP_RESP_InvalidStorageID',
	MTP_RESP_InvalidObjectHandle : 'MTP_RESP_InvalidObjectHandle',
	MTP_RESP_DevicePropNotSupported : 'MTP_RESP_DevicePropNotSupported',
	MTP_RESP_InvalidObjectFormatCode : 'MTP_RESP_InvalidObjectFormatCode',
	MTP_RESP_StoreFull : 'MTP_RESP_StoreFull',
	MTP_RESP_ObjectWriteProtect : 'MTP_RESP_ObjectWriteProtect',
	MTP_RESP_StoreReadOnly : 'MTP_RESP_StoreReadOnly',
	MTP_RESP_AccessDenied : 'MTP_RESP_AccessDenied',
	MTP_RESP_NoThumbnailPresent : 'MTP_RESP_NoThumbnailPresent',
	MTP_RESP_PartialDeletion : 'MTP_RESP_PartialDeletion',
	MTP_RESP_StoreNotAvailable : 'MTP_RESP_StoreNotAvailable',
	MTP_RESP_SpecificiationByFormatUnsupported : 'MTP_RESP_SpecificiationByFormatUnsupported',
	MTP_RESP_NoValidObjectInfo : 'MTP_RESP_NoValidObjectInfo',
	MTP_RESP_DeviceBusy : 'MTP_RESP_DeviceBusy',
	MTP_RESP_InvalidParentObject : 'MTP_RESP_InvalidParentObject',
	MTP_RESP_InvalidDevicePropFormat : 'MTP_RESP_InvalidDevicePropFormat',
	MTP_RESP_InvalidDevicePropValue : 'MTP_RESP_InvalidDevicePropValue',
	MTP_RESP_InvalidParameter : 'MTP_RESP_InvalidParameter',
	MTP_RESP_SessionAlreadyOpen : 'MTP_RESP_SessionAlreadyOpen',
	MTP_RESP_SpecificationOfDestinationUnsupported : 'MTP_RESP_SpecificationOfDestinationUnsupported',
	MTP_RESP_HardwareError : 'MTP_RESP_HardwareError',
	MTP_RESP_OutOfFocus : 'MTP_RESP_OutOfFocus',
	MTP_RESP_ChangeCameraModeFailed : 'MTP_RESP_ChangeCameraModeFailed',
	MTP_RESP_InvalidStatus : 'MTP_RESP_InvalidStatus',
	MTP_RESP_WbPresentError : 'MTP_RESP_WbPresentError',
	MTP_RESP_DustReferenceError : 'MTP_RESP_DustReferenceError',
	MTP_RESP_ShutterSpeedBulb : 'MTP_RESP_ShutterSpeedBulb',
	MTP_RESP_MirrorUpSequence : 'MTP_RESP_MirrorUpSequence',
	MTP_RESP_CameraModeNotAdjustFnumber : 'MTP_RESP_CameraModeNotAdjustFnumber',
	MTP_RESP_NotLiveView : 'MTP_RESP_NotLiveView',
	MTP_RESP_MfDriveStepEnd : 'MTP_RESP_MfDriveStepEnd',
	MTP_RESP_MfDriveStepInsufficiency : 'MTP_RESP_MfDriveStepInsufficiency',
	MTP_RESP_StoreError : 'MTP_RESP_StoreError',
	MTP_RESP_StoreUnformatted : 'MTP_RESP_StoreUnformatted',
	MTP_RESP_BulbReleaseBusy : 'MTP_RESP_BulbReleaseBusy',
	MTP_RESP_ShutterSpeedTime : 'MTP_RESP_ShutterSpeedTime',
	MTP_RESP_NoTransferList : 'MTP_RESP_NoTransferList',
	MTP_RESP_NoJpegPresent : 'MTP_RESP_NoJpegPresent',
	MTP_RESP_InvalidObjectPropCode : 'MTP_RESP_InvalidObjectPropCode',
	MTP_RESP_InvalidObjectPropFormat : 'MTP_RESP_InvalidObjectPropFormat',
	MTP_RESP_COMMUNICATION_ERROR : 'MTP_RESP_COMMUNICATION_ERROR'
}
def getMtpRespDesc(mtpResponseCode):
	if mtpResponseCode in MtpRespDescDictionary:
		return "{:s}".format(MtpRespDescDictionary[mtpResponseCode])
	else:
		return "Unknown Response Code (0x{:04x})".format(mtpResponseCode)

#
# MTP object format codes
#
MTP_OBJFORMAT_NONE				= 0x0000
MTP_OBJFORMAT_NEF_WithoutMtp	= 0x3000	# Nikon raw file
MTP_OBJFORMAT_Assocation		= 0x3001
MTP_OBJFORMAT_Script			= 0x3002
MTP_OBJFORMAT_DigitalPrintOrder	= 0x3006
MTP_OBJFORMAT_WAV				= 0x3008
MTP_OBJFORMAT_NEF_WithMtp		= 0x3800
MTP_OBJFORMAT_EXIF_or_JPEG		= 0x3801
MTP_OBJFORMAT_JFIF				= 0x3808
MTP_OBJFORMAT_MOV				= 0x300d
MTP_OBJFORMAT_TIFF				= 0x380d
MTP_OBJFORMAT_CR2				= 0xb103	# Canon raw file

MtpObjFormatDescDictionary = {\
	MTP_OBJFORMAT_NONE : 'MTP_OBJFORMAT_NONE',
	MTP_OBJFORMAT_NEF_WithoutMtp : 'MTP_OBJFORMAT_NEF_WithoutMtp',
	MTP_OBJFORMAT_Assocation : 'MTP_OBJFORMAT_Assocation',	
	MTP_OBJFORMAT_Script : 'MTP_OBJFORMAT_Script',
	MTP_OBJFORMAT_DigitalPrintOrder : 'MTP_OBJFORMAT_DigitalPrintOrder',	
	MTP_OBJFORMAT_WAV : 'MTP_OBJFORMAT_WAV',
	MTP_OBJFORMAT_NEF_WithMtp : 'MTP_OBJFORMAT_NEF_WithMtp',	
	MTP_OBJFORMAT_EXIF_or_JPEG : 'MTP_OBJFORMAT_EXIF_or_JPEG',
	MTP_OBJFORMAT_JFIF : 'MTP_OBJFORMAT_JFIF',	
	MTP_OBJFORMAT_MOV : 'MTP_OBJFORMAT_MOV',
	MTP_OBJFORMAT_TIFF : 'MTP_OBJFORMAT_TIFF',
	MTP_OBJFORMAT_CR2 : 'MTP_OBJFORMAT_CR2',
}
def getMtpObjFormatDesc(mtpObjFormat):
	if mtpObjFormat in MtpObjFormatDescDictionary:
		return "{:s} (0x{:04x})".format(MtpObjFormatDescDictionary[mtpObjFormat], mtpObjFormat)
	else:
		return "Unknown ObjFormat (0x{:04x})".format(mtpObjFormat)

#
# MTP storage IDs
#
MTP_STORAGEID_MainSlotEmptyOrUnavail	= 0x10000
MTP_STORAGEID_MainSlotPopulated			= 0x10001
MTP_STORAGEID_SubSlotEmptyOrUnavail		= 0x20000
MTP_STORAGEID_SubSlotPopulated			= 0x20001

MTP_STORAGEID_PresenceBit				= 0x00001	# bit 0 is set if slot is populated

MtpStorageIdDescDictionary = {\
	MTP_STORAGEID_MainSlotEmptyOrUnavail : 'MTP_STORAGEID_MainSlotEmptyOrUnavail',
	MTP_STORAGEID_MainSlotPopulated : 'MTP_STORAGEID_MainSlotPopulated',
	MTP_STORAGEID_SubSlotEmptyOrUnavail : 'MTP_STORAGEID_SubSlotEmptyOrUnavail',
	MTP_STORAGEID_SubSlotPopulated : 'MTP_STORAGEID_SubSlotPopulated'
}
def getMtpStorageIdDesc(mtpStorageId):
	if mtpStorageId in MtpStorageIdDescDictionary:
		return "{:s} (0x{:04x})".format(MtpStorageIdDescDictionary[mtpStorageId], mtpStorageId)
	else:
		return "Unknown StorageId (0x{:04x})".format(mtpStorageId)
	
#
# MTP object assocation types
#
MTP_OBJASSOC_GenericFolder				= 0x0001

MtpObjAssocDescDictionary = {\
	MTP_OBJASSOC_GenericFolder : 'MTP_OBJASSOC_GenericFolder'
}	
def getObjAssocDesc(assocType):
	if assocType in MtpObjAssocDescDictionary:
		return "{:s} (0x{:04x})".format(MtpObjAssocDescDictionary[assocType], assocType)
	else:
		return "No Association or Unknown (0x{:04x})".format(assocType)
		
#
# MTP Data Structures
#
MtpDeviceInfoTuple = namedtuple('MtpDeviceInfoTuple', 'standardVersion vendorExtensionID vendorExtensionVersion, vendorExtensionDescStr \
						operationsSupportedSet eventsSupportedSet devicePropertiesSupportedSet \
						captureFormatsSupportedSet imageFormatsSupportedSet manufacturerStr \
						modelStr deviceVersionStr serialNumberStr')
MptStorageIdsTuple = namedtuple('MptStorageIdsTuple', 'storageIdsList')
MtpStorageInfoTuple = namedtuple('MtpStorageInfoTuple', 'storageType, fileSystemType, accessCapability, maxCapacityBytes \
						 freeSpaceBytes, freeSpaceInImages, storageDescription, volumeLabel')						
MtpObjectInfoTuple = namedtuple('MtpObjectInfoTuple', 'storageId objectFormat protectionStatus	\
						objectCompressedSize thumbFormat thumbCompressedSize \
						thumbPixWidth thumbPixHeight imagePixWidth imagePixHeight \
						imageBitDepth parentObject associationType \
						associationDesc sequenceNumber filename \
						captureDateStr modificationDateStr')
						