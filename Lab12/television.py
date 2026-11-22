class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        This functions sets the variables "status", "muted", "channel", and "volume" to their default status
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        This function sets the variable "status" to True or False which indicates
        whether the television is on or off
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        This function sets the mute variable to True or False which indicates
        whether the television is mute or not
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        '''
        This function turns the channel one station up and back to the
        min television channel if channel up is selected at the max television channel
        '''
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        This function turns the channel one station down and back to the
        max television channel if channel down is selected at the min television channel
        '''
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        This function turns the television volume up by one up until the max television volume
        '''
        if self.__status == True:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            if self.__muted == True:
                self.__muted = False

    def volume_down(self) -> None:
        '''
        This function turns down the television volume up until the min television volume
        '''
        if self.__status == True:
            self.__volume -= 1
            if self.__muted == True:
                self.__muted = False
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        '''
        This function displays the television status, channel, and volume
        :return: The result of the power, channel, and volume
        '''
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'