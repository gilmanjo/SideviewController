# Handler for FLIR cameras using their proprietary PySpin wrapper
# Look into their PySpin API for implementation details, much of this code
# is copy-pasted in :)
import constants
import cv2
import PySpin
import time
import numpy as np


class ImageEventHandler(PySpin.ImageEvent):

    def __init__(self, flir_cam, cam, output_loc, im_passback):

        super(ImageEventHandler, self).__init__()

        nodemap = flir_cam.GetTLDeviceNodeMap()

        # Set internal state
        self.rec_state = constants.STATE_MW_IDLE
        self.recording = False
        self.cam = cam
        self.output_loc = output_loc
        self.im_passback = im_passback

        # Save dimensions
        self.height = flir_cam.Height()
        self.width = flir_cam.Width()

        self.timer = time.time()

        # Retrieve device serial number
        node_device_serial_number = PySpin.CStringPtr(
            nodemap.GetNode('DeviceSerialNumber'))

        if PySpin.IsAvailable(node_device_serial_number) and PySpin.IsReadable(
                node_device_serial_number):
            self._device_serial_number = node_device_serial_number.GetValue()

        del flir_cam

    def _init_videowriter(self):
        # OpenCV implementation
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        output_fn = "{}_SIDEVIEW_CAM_{}".format(
            int(time.time()),
            self.cam.name
        )
        self.output = cv2.VideoWriter(
            "{}\{}{}".format(
                self.output_loc,
                output_fn,
                constants.OUTPUT_FILE_EXT
            ),
            fourcc,
            constants.CAM_FPS,
            (self.width,
             self.height),
            isColor=False
        )

    def _to_np(self, image):
        # Converts an ImagePtr to a NumPy array
        data = image.GetData()
        np_image = data.reshape((
            self.height,
            self.width
        ))
        return np_image

    def OnImageEvent(self, image):
        """This method defines an image event. In it, the image that triggered
        the event is converted and saved before incrementing the count. Please
        see Acquisition example for more in-depth comments on the acquisition
        of images.

        :param image: Image from event.
        :type image: ImagePtr
        :rtype: None
        """
        frame = self._to_np(image)

        # Initialize VideoWriter if recording starts
        if self.rec_state == constants.STATE_MW_RUN \
                and self.recording is False:
            self.recording = True
            self._init_videowriter()

        # Add frames if recording
        if self.rec_state == constants.STATE_MW_RUN and self.output != None:
            self.output.write(frame)

        # Add text overlay
        if self.recording:
            cv2.putText(frame, constants.OVERLAY_REC,
                        constants.OVERLAY_FONT_POINT_LARGE,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        constants.OVERLAY_FONT_SCALE_LARGE,
                        constants.OVERLAY_FONT_REC_COLOR,
                        constants.OVERLAY_FONT_THICKNESS
                        )
        else:
            cv2.putText(frame, constants.OVERLAY_IDLE,
                        constants.OVERLAY_FONT_POINT_LARGE,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        constants.OVERLAY_FONT_SCALE_LARGE,
                        constants.OVERLAY_FONT_IDLE_COLOR,
                        constants.OVERLAY_FONT_THICKNESS
                        )

        # Release file if recording ends
        if self.recording and self.rec_state == constants.STATE_MW_IDLE \
                and self.output != None:
            self.recording = False
            self.output.release()

        self.im_passback.emit(self.cam, frame)
