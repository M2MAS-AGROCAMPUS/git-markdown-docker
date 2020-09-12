# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: jl:light,notebooks//ipynb
#     text_representation:
#       extension: .jl
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Julia 1.5.0
#     language: julia
#     name: julia-1.5
# ---

# # Example Julia
#
# ## Documentation de fonction

"""
    bspline(p, j, x)

Return the value at x in [0,1[ of the B-spline with integer nodes of degree p with support starting at j.
Implemented recursively using the [De Boor's Algorithm](https://en.wikipedia.org/wiki/De_Boor%27s_algorithm)

```math
B_{i,0}(x) := \\left\\{
\\begin{matrix}
1 & \\mathrm{if}  \\quad t_i ≤ x < t_{i+1} \\\\
0 & \\mathrm{otherwise} 
\\end{matrix}
\\right.
```

```math
B_{i,p}(x) := \\frac{x - t_i}{t_{i+p} - t_i} B_{i,p-1}(x) 
+ \\frac{t_{i+p+1} - x}{t_{i+p+1} - t_{i+1}} B_{i+1,p-1}(x).
```
"""
function bspline(p::Int, j::Int, x::Float64)
   if p == 0
       if j == 0
           return 1.0
       else
           return 0.0
       end
   else
       w = (x - j) / p
       w1 = (x - j - 1) / p
   end
   return (w * bspline(p - 1, j, x) + (1 - w1) * bspline(p - 1, j + 1, x))
end

# Switch the next cell from `Markdown` to `Code` format

# ?bspline

# +
using Random, Plots

function generate_data( n = 2000, seed = 1234 )
    seuil = 0.25
    rng = MersenneTwister(seed)
    X1 = rand( rng, n)
    X2 = rand( rng, n)
    U  = rand( rng, n)
    Y  = zeros(Int,n)
    Y[(X1 .<= 0.25) .& (U  .<= seuil)] .= 1
    Y[(X1 .>  0.25) .& (X2 .>= 0.75) .& (U .<= seuil)] .= 1
    Y[(X1 .>  0.25) .& (X2 .<  0.75) .& (U .>  seuil)] .= 1
    return X1, X2, Y
end

X1, X2, Y = generate_data()
scatter(X1,X2, marker_z = Y)
# -
using DataFrames, StatsPlots

data = DataFrame( X1=X1, X2=X2, Y=Y)
head(data)

@df data scatter(:X1,:X2, zcolor= :Y, xaxis = "X1", yaxis="X2", lab="Y")


"""
[x1,x2,x1^2,x1x2,x2^2……x2^6]
"""
function map_features(X1,X2)
    degree = 6
    out = ones(size(X1[:,1]))
    for i=1:6
        for j=0:i
            out = hcat(out,(X1.^(i-j)).*(X2.^j))
        end
    end
    return out
end

X = map_features(X1,X2)


