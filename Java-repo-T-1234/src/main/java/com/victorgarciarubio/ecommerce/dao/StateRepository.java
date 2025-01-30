package com.victorgarciarubio.ecommerce.dao;

import java.util.List;

import com.victorgarciarubio.ecommerce.entity.State;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;

@CrossOrigin(origins = {"https://ecommerce-angular-app.victorgarciar.com", "https://frontend-ecommerce-angular.vercel.app"})
@RepositoryRestResource(collectionResourceRel = "states", path="states")
@Api(tags = "State Repository", description = "Operations pertaining to states in the e-commerce application")
public interface StateRepository extends JpaRepository<State, Integer> {
    
    @ApiOperation(value = "Find states by country code", notes = "Returns a list of states for a given country code")
    @ApiParam(name = "code", value = "Country code to filter states", required = true)
    List<State> findByCountryCode(@Param("code") String code);
}