class Solution:
    def binarysearchasc(self,l,r,mountainArr,target):
        while(l<=r):
            mid=(l+r)//2
            if(mountainArr.get(mid)>target):
                r=mid-1
            elif(mountainArr.get(mid)<target):
                l=mid+1
            else:
                return mid
        return -1
    def binarysearchdesc(self,l,r,mountainArr,target):
        while(l<=r):
            mid=(l+r)//2
            if(mountainArr.get(mid)>target):
                l=mid+1
                
            elif(mountainArr.get(mid)<target):
                r=mid-1
            else:
                return mid
        return -1
    


    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r= 0 ,mountainArr.length()-1
        while(l<=r):
            mid=(l+r)//2
            if(mid>0 and mountainArr.get(mid)<mountainArr.get(mid-1)):
                r=mid-1
            elif(mid<mountainArr.length()-1 and  mountainArr.get(mid)<mountainArr.get(mid+1) ):
                l=mid+1
            else:
                break
        peak=mid
        print(peak)

        out=self.binarysearchasc(0,mid,mountainArr,target)
        print(out)
        if(out!=-1):
            return out
        else:
            out=self.binarysearchdesc(mid+1,mountainArr.length()-1,mountainArr,target)
            return out


        