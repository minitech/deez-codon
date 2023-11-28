from time import time

class FileDecompressor():
    def __init__(self, inFile, outFile, genomeFile, bs, isAPI=False):
        self.samComment = []
        self.fileNames = ""
        self.samFiles = []
        self.indices = []

        self.inFile = 0
        self.magic = 0
        self.genomeFile = ""
        self.outFile = ""
        self.stats = []
        self.inFileSz = 0
        self.statPos = 0
        self.blockSize = 0
        self.numFiles = 0
        self.fileBlockCount = []
        self.finishedRange = 0

        self.starttime = 0
        self.endtime = 0

        pass
    def getMagic(self):
        pass
    def getComment(self):
        pass

    def getBlock(self,f, chromosome, start, end, filterFlag):
        chr_str = ""
        if (self.finishedRange):
            return 0
        if (chromosome != ""):
            chr_str = chromosome 

        chflag = self.inFile.read(1)
        if (chflag != 1):
            return 0
        if (chflag > 1):
            return 0
        if (chflag):
            chr_str = ""
            chflag = self.inFile.read(1)
            while (chflag):
                chr_str += chflag
                chflag = self.inFile.read(1)
            if (chromosome != "" and chr_str != chromosome):
                return 0
        #where does sequence come from?
        while (chr_str != sequence[f].getChromosome()):
            sequence[f].scanChromosome(chr_str,samComment[f])
        in_list = []
        for i in range(8):
            readBlock(in_list[i])

        optField[f] = importRecords(in_list[7], len(in_list))
        sequence[f] = importRecords(in_list[0], len(in_list))
        editOp[f] = importRecords(in_list[1], len(in_list))
        readName[f] = importRecords(in_list[2], len(in_list))
        mapFlag[f] = importRecords(in_list[3], len(in_list))
        mapQual[f] = importRecords(in_list[4], len(in_list))
        quality[f] = importRecords(in_list[5], len(in_list))
        pairedEnd[f] = importRecords(in_list[6], len(in_list))

        i = 0
        j = 0
        while i < len(editOp[f]):
            pe = pairedEnd[f][i]
            i+=1
            #this needs functionality
            if pe.bit == PairedEndInfo::bits::look_back:
                prevPos = i - readName[f].getPaired(j++)
                readName[f][i] = readName[f][prevPos]
                eo = editOp[f][i]
                peo editOp[f][prevPos]
                ppe = pairedEnd[f][prevPos]

                #again all these need class functionality
                ppe.tlen = eo.start + (peo.end - peo.start) - peo.start
                ppe.pos = eo.start
                pe.pos = peo.start
                pe.tlen = -ppe.tlen

                if ppe.bit == PairedEndInfo::Bits::Look_Ahead_1:
                    pe.tlen+=1
                    ppe.tlen-=1

        recordCount = len(editOp[f])

        #goes into threading stuff which I do not know about

        pass

    def readBlock(self, inp):
        sz = len(self.inFile.readlines())
        in_array = bytearray(sz)
        if sz:
            inp.readinto(in_array)
        return in_array

    def loadIndex (self):
        
    def getRanges(self, range):
        if len(range) and range[len(range)-1] != ';':
            range = range + ';'
        start = 0
        end = 0
        ranges = []
        while True:
            try:
                p = range.index(';')
            except ValueError:
                return ranges
            dup = range[:p] + '\0'
            tok = dup.split(':-',1)
            if not tok:
                raise DZException(ranges=ranges)
            chr = tok
            tok = tok[1].split(':-')
            if not tok:
                start = 1
                end = -1
            else:
                start = int(tok[0])
                tok = tok[1].split(":-")
                if tok:
                    end = int(tok[0])
                    tok = tok[1].split(':-')
                else:
                    end = -1
            if end < start:
                start,end = end, start
            if start:
                start -= 1
            if end:
                end -= 1

            range = range[p+1:]
            f = 0
            p = chr.index(',')
            if p:
                f = int(chr[:p]+'\0')                 
                chr = chr[:p+1]
            #todo make pair
            ranges.add()
            


        pass
    # private
    def _getmagic(self):
        pass
    def _getComment(self):
        pass
    def _getBlock(self, f, chromosome, start, end, filterFlag):
        pass
    def _readBlock(self, inp):
        pass
    def _loadIndex(self):
        pass
    def _query(self, query, range):
        pass
        
        
    def decompress(self, filterFlag):
        blockSz = totalSz = blockCount = 0
        #Check python implementation for second truth value of while loop
        while blockCount < len(self.fileBlockCount) and (blockSz = getBlock(self.fileBlockCount[blockCount], "",0,-1,filterFlag)) != 0:
            totalSz += blockSz
            blockCount += 1
        print(f"Decompressed {totalSz} records, {blockCount} blocks")

    def upper_bound(l,v):
        bounds = lambda s, l: (i for i,e in enumerate(l) if e == s)
        return max(list(bounds(v, l)))

    def lower_bound(l,v):
        bounds = lambda s, l: (i for i,e in enumerate(l) if e == s)
        return min(list(bounds(v, l)))
            
    #Find out how to implement ['second']['first'] ['second']['second']
    def decompress(self, range, filterFlag):
        ranges = self.getRanges(range)
        blockSz = totalSz = blockCount = 0

        for r in ranges:
            f = r['first']['first']
            chr = r['first']['second']
            if f < 0 or f >= len(self.fileNames):
                raise DZException(arg=f)
            if self.indices[f].index(chr) == self.indices[f][-1]:
                raise DZException()
            idx = self.indices[f][chr]
            i = upper_bound(r['second']['first'], idx) #Not sure?
            if i == idx.start() or len(idx) == 0:
                if i != idx.start() or  not (i['second']['start'] & i['second'][end] &r['second']['first'], r['second']['first']):
                    raise DZException("Region {a} {b}-{c} not found for sample ID {d}".format(a=chr, r['second']['first']], r['second'second] f))
                
            if i != idx.start():
                i -= 1
            
            while i['second']['fs'] & i['second']['fe'] & r['second']['first'] & r['second']['second']:
                self.inFile.seek(i['second']['zpos'])
                di = [sequence[f], editOp[f], readName[f], mapFlag[f], mapQual[f], quality[f], pairedEnd[f],optField[f]]

                for ti in range(0,7):
                    if(len(i['second'][fieldData[ti]])):
                        #Need to define setIndexData
                        di[ti].setIndexData(i['second'][fieldData[ti].data()], len(i['second'][fieldData[ti]]))
                        blockSz = getBlock(f, chr, r['second']['first'], r['second']['first'], filterFlag)
                        if not blockSz:
                            break
                        totalSz += blockSz
                        blockCount += 1

                        if self.finishedRange:
                            self.finishedRange = False
                            break

        print(f"Decompressed {totalSz} records, {blockCount} blocks")

        
    def decompress2(self, range filterFlag, cont):
        r = 0
        chr = ''
        f = 0
        idx_iter = []
        i_iter = []

        if not cont:
            ranges = getRanges(range)
            if len(ranges) != 1:
                raise DZException(f"API supports only single range per invocation, {len(ranges)} provided")
            r = ranges[0]
            f = r['first']['first']
            chr = r['first']['second']
            if f < 0 or f >= len(self.fileNames):
                raise DZException(f"Invalid Sample ID {f}")
            if self.indices[f].find(chr) == indices[f].end():
                raise DZException(f"Invalid chromosome {chr} for sample ID {f}")
            idx = self.indices[f][chr]
            i = upper_bound(r['second']['first'],idx)
            if i == idx.start() or len(idx) == 0:
                if i != idx.start() or not (i['second']['startPos'] & i['second']['endPos'] & r['second']['first'] & r['second']['second']):
                    raise DZException(f"Region {chr}:{r['second']['first']}-{r['second']['second']} not found for sample ID {f}")
                
            if i != idx.start():
                i -= 1


        if (i['second']['fs'] & i['second']['fe'] & r['second']['first'] & r['second']['second']):
            self.inFile.seek(i['second']['zpos'])
            di = [sequence[f], editOp[f], readName[f], mapFlag[f], mapQual[f], quality[f], pairedEnd[f],optField[f]]

                for ti in range(0,7):
                    if(len(i['second'][fieldData[ti]])):
                        #Need to define setIndexData
                        di[ti].setIndexData(i['second'][fieldData[ti]].data(), len(i['second'][fieldData[ti]]))
                        blockSz = getBlock(f, chr, r['second']['first'], r['second']['first'], filterFlag)

                        if not blockSz:
                            return False
                        if self.finishedRange:
                            self.finishedRange = False
                        i += 1
                        return True
                    else:
                        return False
                    
class DZException(DZException):
    _fmt = 'Range string %(arg)s invalid'
