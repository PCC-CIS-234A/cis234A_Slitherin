# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        This file handles the logic involved with sending
#                       email notifications
# Sources:          	Project Specifications
# *****************************************************************************
import Database as d


def get_email_list():
    return d.Database.build_email_list()
