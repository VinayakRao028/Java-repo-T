package com.victorgarciarubio.ecommerce.dao;

import com.victorgarciarubio.ecommerce.entity.Country;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"https://ecommerce-angular-app.victorgarciar.com", "https://frontend-ecommerce-angular.vercel.app"})
@RepositoryRestResource(collectionResourceRel = "countries", path="countries")
@Api(tags = "Country", description = "Operations pertaining to countries in the e-commerce application")
public interface CountryRepository extends JpaRepository<Country, Integer> {
    
    @ApiOperation(value = "Find all countries", notes = "Returns a list of all countries")
    @Override
    Iterable<Country> findAll();

    @ApiOperation(value = "Find country by ID", notes = "Returns a single country")
    @Override
    Country findById(Integer id);

    @ApiOperation(value = "Save a country", notes = "Saves a new country or updates an existing one")
    @Override
    <S extends Country> S save(S entity);

    @ApiOperation(value = "Delete a country", notes = "Deletes a country by its ID")
    @Override
    void deleteById(Integer id);
}