package com.victorgarciarubio.ecommerce.dao;

import com.victorgarciarubio.ecommerce.entity.ProductCategory;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"https://ecommerce-angular-app.victorgarciariar.com", "https://frontend-ecommerce-angular.vercel.app"})
@RepositoryRestResource(collectionResourceRel = "productCategory", path = "product-category")
@Api(tags = "Product Category", description = "Operations pertaining to product categories in the e-commerce application")
public interface ProductCategoryRepository extends JpaRepository<ProductCategory, Long> {
    
    @ApiOperation(value = "Get all product categories", notes = "Retrieves a list of all product categories")
    @Override
    Iterable<ProductCategory> findAll();

    @ApiOperation(value = "Get a product category by ID", notes = "Retrieves a single product category by its ID")
    @Override
    ProductCategory findById(Long id);

    @ApiOperation(value = "Save a product category", notes = "Creates a new product category or updates an existing one")
    @Override
    <S extends ProductCategory> S save(S entity);

    @ApiOperation(value = "Delete a product category", notes = "Deletes a product category by its ID")
    @Override
    void deleteById(Long id);
}