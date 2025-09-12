import math
def cosine_similarity(vec1, vec2):
    pair_vectors=zip(vec1, vec2)
    products=[]
    for a,b in pair_vectors:
        products.append(a*b)
    dot_product=sum(products)

    mag1=math.sqrt(sum(a**2 for a in vec1))
    mag2=math.sqrt(sum(b**2 for b in vec2))
    cosine_sim=dot_product/(mag1*mag2)
    print("cosine similarity:",cosine_sim)

def main():
    vec1=[3,4]
    vec2=[4,5]
    cosine_similarity(vec1,vec2)
if __name__=="__main__":
    main()

 