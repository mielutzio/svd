# Singular Value Decomposition (SVD) 

Let 
$ A \in \mathbb{R}^{n,m} $.
Then svd decomposition of _A_ is a product of three matrices 
$ U \Sigma V^{T} $,
where : 
  -  $ U \in \mathbb{R}^{n,r} $ 
     is orthogonal, with right singular vectors (rotation)
  -  $ \Sigma \in \mathbb{R}^{r,r} $ 
     is diagonal, with singular values (stretch)
  -  $ V^T \in \mathbb{R}^{r,m} $
     is orthogonal, with left singular vectors (rotation) .
     
 ![circle](https://github.com/lucianodainic/svd/blob/main/assets/circle.png)
 
 :orange_circle: left singular vectors
 
 ![ellipse](https://github.com/lucianodainic/svd/blob/main/assets/ellipse.png)
 
 Circle
 $ * \Sigma $
 = Ellipse
 
 :orange_circle: 
singular values with origin form the semi axes
 
 ![rotated_ellipse](https://github.com/lucianodainic/svd/blob/main/assets/rotated_ellipse.png)
 
 _U_ * Ellipse = Rotation
 
 :orange_circle: 
 $ \Sigma * U $
 new values for the semi axes of the rotated ellipse 
