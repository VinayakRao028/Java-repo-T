package com.victorgarciarubio.ecommerce.dao;

import com.victorgarciarubio.ecommerce.entity.Product;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestParam;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;

@CrossOrigin(origins = {"https://ecommerce-angular-app.victorgarciar.com", "https://frontend-ecommerce-angular.vercel.app"})
@RepositoryRestResource(collectionResourceRel = "products", path = "products")
@Api(tags = "Product Repository", description = "Operations pertaining to products in the e-commerce application")
public interface ProductRepository extends JpaRepository<Product, Long> {

    @ApiOperation(value = "Find products by category ID", notes = "Returns a page of products belonging to a specific category")
    @ApiParam(name = "id", value = "Category ID", required = true)
    Page<Product> findByCategoryId(@RequestParam("id") Long id, Pageable pageable);

    @ApiOperation(value = "Find products by name", notes = "Returns a page of products whose names contain the given string")
    @ApiParam(name = "name", value = "Product name to search for", required = true)
    Page<Product> findByNameContaining(@RequestParam("name") String name, Pageable pageable);
}