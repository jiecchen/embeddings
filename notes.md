
# what binaries to create?

## GraphCoarsening
input: 
 - network_file of G_i
output: 
 - network_file of G_{i+1}: the file of coarsened network 
 - mapping_file from i+1 to i: in the format of 
   1, a1, a2, ...
   2, b1, b2, ...
   3, c1, c2, ...
 

## ExpandEmbedding
input:
 - embedding_file of G_{i+1}, mapping_file from i to i+1
output:
 - initial values of embeddings of G_i

## InitEmbeddings
this depends on the implementation of each embedding algorithms.
   - currently we have solution to LINE
   - don't know how to handle DeepWalk or Node2Vec. They use genism.models.word2vec, can not set the initial values
   
   

# TODO
- implement code to test the embedding results

