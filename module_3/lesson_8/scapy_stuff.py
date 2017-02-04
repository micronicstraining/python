# scapy wireshark labs experiments
#             * Scapy & Wireshark - Packet construction and manipulation 
#                 * https://www.netzob.org/ reverse engineer packets 
#                 * Langley’s Law (Protocol testing should be done with broken packets) 
#                 * https://blog.gerv.net/2016/09/introducing-deliberate-protocol-errors-langleys-law/ 
#                 * https://www.ixiacom.com/company/blog/equation-groups-firewall-exploit-chain 
#                 * https://www.netzob.org/ 
#
# - basic
# - intermediate
# - advanced - https://github.com/NullHypothesis/backlogscans
# - very advanced - https://www.ixiacom.com/company/blog/equation-groups-firewall-exploit-chain
#
#             * Homework http://pytbull.sourceforge.net/ test firewall payloads? 
#                 * Generate pcap broken & working with wireshark 
#                     * Bonus if based on real exploit 
#                 * Test it with pybull 
#                     * Bonus if you submit it to pytbull repo 



# get all commands
# ICMP echo example
#
# sr1
# Welcome to Scapy (2.2.0)
# >>> sr1(IP(dst='8.8.8.8')/UDP()/DNS(rd=1,qd=DNSQR(qname='packetlife.net')))
# Begin emission:
# Finished to send 1 packets.
